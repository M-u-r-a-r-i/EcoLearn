// Typed client for the EcoLearn FastAPI backend.
//
// Every call to the backend goes through a function here, so the rest of the app
// never writes raw fetch() calls or hardcodes URLs. This mirrors the Python side:
// the UI talks to ONE module, and that module talks to the network.
//
// Who the student is travels in an httpOnly session cookie that the API sets at
// login. JavaScript can't read it (that's the point: a script injected into the
// page can't steal it), so no function here takes a student id — the browser
// attaches the cookie itself because every request uses credentials: "include".

// The base URL comes from the environment (web/.env.local). We fall back to
// localhost so the app still runs if the var is missing in development.
//
// Local development: the API must be on the SAME host name as the page.
// localhost and 127.0.0.1 count as different sites, and the session cookie
// (SameSite=Lax) is not sent between different sites — so a page opened at
// 127.0.0.1:3000 calling localhost:8000 logged in, lost the cookie, and was
// sent straight back to the login page. When both are a loopback name, follow
// whichever one the page was opened with.
function resolveApiUrl(): string {
  const configured = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
  if (typeof window === "undefined") return configured;
  try {
    const url = new URL(configured);
    const loopback = ["localhost", "127.0.0.1"];
    if (loopback.includes(url.hostname) && loopback.includes(window.location.hostname)) {
      url.hostname = window.location.hostname;
    }
    return `${url.protocol}//${url.host}`;
  } catch {
    return configured;
  }
}

export const API_URL = resolveApiUrl();

// ---------------------------------------------------------------------------
// The one request helper.
// ---------------------------------------------------------------------------

// An HTTP error from the API, carrying the status and FastAPI's {"detail"} text.
// status 0 means the request never got an answer (backend down, timeout, CORS).
export class ApiError extends Error {
  constructor(
    public status: number,
    public detail: string,
  ) {
    super(detail);
    this.name = "ApiError";
  }
}

// Called on any 401 from a request that expected a session, so the auth provider
// can drop the user back to the login page. A callback instead of a router
// import keeps this module free of React.
let onUnauthorized: (() => void) | null = null;
export function setUnauthorizedHandler(handler: (() => void) | null) {
  onUnauthorized = handler;
}

interface RequestOptions {
  method?: "GET" | "POST" | "PATCH" | "PUT";
  query?: Record<string, string | undefined>;
  body?: unknown;
  timeoutMs?: number;
  // Login and "who am I" answer 401 as a normal outcome; don't treat it as expiry.
  expectAuthFailure?: boolean;
}

// Live-LLM calls (the doubt chat) take seconds; everything else is cached.
const DEFAULT_TIMEOUT_MS = 15_000;
const LIVE_TIMEOUT_MS = 90_000;

async function request<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const url = new URL(`${API_URL}${path}`);
  for (const [key, value] of Object.entries(options.query ?? {})) {
    if (value !== undefined) url.searchParams.set(key, value);
  }

  let response: Response;
  try {
    response = await fetch(url, {
      method: options.method ?? "GET",
      credentials: "include", // send the session cookie to the API's origin
      headers: options.body === undefined ? undefined : { "Content-Type": "application/json" },
      body: options.body === undefined ? undefined : JSON.stringify(options.body),
      signal: AbortSignal.timeout(options.timeoutMs ?? DEFAULT_TIMEOUT_MS),
    });
  } catch {
    // fetch() only throws when there is no HTTP answer at all.
    throw new ApiError(0, "Can't reach EcoLearn right now. Check your connection and try again.");
  }

  // fetch() does NOT throw on 4xx/5xx, so check response.ok ourselves.
  if (!response.ok) {
    const detail = await readDetail(response);
    if (response.status === 401 && !options.expectAuthFailure) onUnauthorized?.();
    throw new ApiError(response.status, detail);
  }
  return (await response.json()) as T;
}

// FastAPI errors look like {"detail": "..."} — or, for a 422, a list of problems.
async function readDetail(response: Response): Promise<string> {
  try {
    const data = await response.json();
    if (typeof data?.detail === "string") return data.detail;
    if (Array.isArray(data?.detail)) return "Please check the form and try again.";
  } catch {
    // not JSON — fall through
  }
  return response.status >= 500
    ? "Something went wrong on our side. Please try again."
    : `Request failed (${response.status}).`;
}

// A message that is safe to show a student for any error thrown here.
export function friendlyMessage(error: unknown): string {
  if (error instanceof ApiError) return error.detail;
  return "Something went wrong. Please try again.";
}

// ---------------------------------------------------------------------------
// Accounts
// ---------------------------------------------------------------------------
export interface StudentProfile {
  student_id: string;
  username: string | null; // null only for legacy name-only (Streamlit) students
  name: string;
  interest: string;
  level: string;
  created_at: string;
}

export interface RegisterInput {
  name: string;
  username: string;
  password: string;
  interest: string;
  level: string;
}

export function register(input: RegisterInput): Promise<StudentProfile> {
  return request("/api/auth/register", { method: "POST", body: input });
}

export function login(username: string, password: string): Promise<StudentProfile> {
  return request("/api/auth/login", {
    method: "POST",
    body: { username, password },
    expectAuthFailure: true,
  });
}

export function logout(): Promise<{ logged_out: boolean }> {
  return request("/api/auth/logout", { method: "POST" });
}

// 200 with the profile when the session cookie is valid, ApiError(401) otherwise.
export function getMe(): Promise<StudentProfile> {
  return request("/api/auth/me", { expectAuthFailure: true });
}

export function updateProfile(
  changes: Partial<Pick<StudentProfile, "name" | "interest" | "level">>,
): Promise<StudentProfile> {
  return request("/api/profile", { method: "PATCH", body: changes });
}

export function changePassword(currentPassword: string, newPassword: string): Promise<unknown> {
  return request("/api/auth/change-password", {
    method: "POST",
    body: { current_password: currentPassword, new_password: newPassword },
    expectAuthFailure: true, // a wrong current password is a 401 too, not an expired session
  });
}

// ---------------------------------------------------------------------------
// Who is logged in, and as what. One question on page load instead of probing
// the student and teacher endpoints separately.
// ---------------------------------------------------------------------------
export type Session =
  | { role: "student"; profile: StudentProfile }
  | { role: "teacher"; profile: TeacherProfile };

export function getSession(): Promise<Session> {
  return request("/api/auth/session", { expectAuthFailure: true });
}

// ---------------------------------------------------------------------------
// Teachers. Teacher accounts are created on the server (scripts/create_teacher.py),
// never from the website. A teacher sees only their own classes.
// ---------------------------------------------------------------------------
export interface TeacherProfile {
  teacher_id: string;
  name: string;
  username: string;
  created_at: string;
}

export interface ClassSummary {
  class_id: string;
  teacher_id: string;
  name: string;
  level: string;
  created_at: string;
  student_count: number;
}

// A freshly created (or reset) student login. The password exists in plaintext
// only in this one response — the server keeps just its hash.
export interface StudentCredential {
  student_id: string;
  name: string;
  username: string;
  password: string;
  interest?: string;
}

export interface CredentialsResult {
  class: ClassSummary;
  credentials: StudentCredential[];
}

export interface ClassStudent {
  student_id: string;
  name: string;
  username: string;
  interest: string;
  level: string;
  created_at: string;
  attempted: number; // concepts tried at least once
  mastered: number;
  last_active: string | null; // ISO time of the latest attempt, null if none yet
}

export interface ClassDetail {
  class: ClassSummary;
  students: ClassStudent[];
}

// Creating accounts hashes every password (deliberately slow) — a full class
// takes several seconds, so these calls get the long timeout.
const ACCOUNTS_TIMEOUT_MS = LIVE_TIMEOUT_MS;

export function teacherLogin(username: string, password: string): Promise<TeacherProfile> {
  return request("/api/teacher/login", {
    method: "POST",
    body: { username, password },
    expectAuthFailure: true,
  });
}

export function changeTeacherPassword(currentPassword: string, newPassword: string): Promise<unknown> {
  return request("/api/teacher/change-password", {
    method: "POST",
    body: { current_password: currentPassword, new_password: newPassword },
    expectAuthFailure: true,
  });
}

export function getClasses(): Promise<ClassSummary[]> {
  return request("/api/teacher/classes");
}

export interface CreateClassInput {
  name: string;
  level: string;
  interest: string;
  roster: string; // one name per line, optionally "Name, interest"
}

export function createClass(input: CreateClassInput): Promise<CredentialsResult> {
  return request("/api/teacher/classes", {
    method: "POST",
    body: input,
    timeoutMs: ACCOUNTS_TIMEOUT_MS,
  });
}

export function getClassDetail(classId: string): Promise<ClassDetail> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}`);
}

export function addStudents(
  classId: string,
  roster: string,
  interest: string,
): Promise<CredentialsResult> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/students`, {
    method: "POST",
    body: { roster, interest },
    timeoutMs: ACCOUNTS_TIMEOUT_MS,
  });
}

// Only a teacher can move a student between Class 11 and Class 12.
export function setStudentLevel(studentId: string, level: string): Promise<{ student_id: string; level: string }> {
  return request(`/api/teacher/students/${encodeURIComponent(studentId)}/level`, {
    method: "POST",
    body: { level },
  });
}

export function resetStudentPassword(studentId: string): Promise<StudentCredential> {
  return request(`/api/teacher/students/${encodeURIComponent(studentId)}/reset-password`, {
    method: "POST",
  });
}

// ---------------------------------------------------------------------------
// Class insights: the pilot metrics and the misconception view for a teacher.
// Fractions (accuracy, share, approval) are 0–1, or null when nothing to divide.
// ---------------------------------------------------------------------------
export interface InsightSummary {
  students: number;
  active_students: number;
  lessons_opened: number;
  distinct_lessons: number;
  active_minutes: number;
  median_minutes_per_lesson: number | null;
  answers: number;
  first_try_answers: number;
  first_try_correct: number;
  first_try_accuracy: number | null;
  thumbs_up: number;
  thumbs_down: number;
  approval: number | null;
  // First tries by "how sure are you?"; accuracy is 0–1 or null.
  by_confidence: Record<Confidence, { answers: number; accuracy: number | null }>;
  sure_but_wrong: number;
}

// One wrong option and the misconception it reveals, counted in students.
export interface MisconceptionInsight {
  concept_id: string;
  concept_name: string;
  interest: string;
  question: string | null; // markdown
  option: string;
  option_text: string | null; // markdown
  correct_option: string | null;
  correct_text: string | null; // markdown
  misconception: string | null;
  students: number; // students who chose this option
  sure: number; // of those, how many were sure (a firmly held misconception)
  student_ids: string[]; // which ones (this teacher's own students)
  students_answered: number; // students who answered this question
  share: number | null;
}

export interface ConceptInsight {
  concept_id: string;
  concept_name: string;
  chapter_id: string | null;
  chapter_name: string | null;
  students_opened: number;
  students_answered: number;
  first_try_correct: number;
  first_try_accuracy: number | null;
  median_minutes: number | null;
  thumbs_up: number;
  thumbs_down: number;
}

export interface InterestInsight {
  interest: string;
  students: number;
  lessons_opened: number;
  first_try_accuracy: number | null;
  thumbs_up: number;
  thumbs_down: number;
  approval: number | null;
}

export interface StudentInsight {
  student_id: string;
  name: string;
  username: string;
  interest: string;
  lessons_opened: number;
  active_minutes: number;
  answered: number; // first tries
  first_try_correct: number;
  first_try_accuracy: number | null;
  thumbs_up: number;
  thumbs_down: number;
}

export interface ClassInsights {
  class: ClassSummary;
  summary: InsightSummary;
  misconceptions: MisconceptionInsight[];
  concepts: ConceptInsight[];
  interests: InterestInsight[];
  students: StudentInsight[];
}

export function getClassInsights(classId: string): Promise<ClassInsights> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/insights`);
}

// ---------------------------------------------------------------------------
// The teaching assistant: an agent that reads the class's data and plans the
// next lesson. Falls back to a rules-based plan when no model is available.
// ---------------------------------------------------------------------------
export interface ClassPlan {
  plan_id: number;
  created_at: string;
  source: "agent" | "rules";
  model: string | null;
  note: string | null; // why it's a rules plan, when it is
  markdown: string; // five sections, student names already filled in
  steps: { summary: string; ok: boolean }[]; // what the agent looked at
  reused?: boolean; // true if a plan from the last minute was returned
}

// ---------------------------------------------------------------------------
// "How the AI decided": every guardrail at work in a class, and each personal
// story's step-by-step record (rule checks, the critic's verdict, rewrites).
// ---------------------------------------------------------------------------
export type DecisionStep = "format" | "fit" | "rules" | "critic" | "model";

export interface DecisionTrailStep {
  attempt: number;
  step: DecisionStep;
  passed: boolean;
  problems: string[];
  model: string | null;
}

export interface AiDecisions {
  stories: {
    attempted: number;
    shown: number;
    first_draft: number;
    rewritten: number;
    blocked: number;
    declined: number;
    errors: number;
    reported: number;
    hidden_by_teacher: number;
    rules_rejections: number;
    critic_checks: number;
    critic_rejections: number;
  };
  plans: { total: number; agent: number; rules: number; latest_note: string | null };
  calls: {
    total: number;
    failed: number;
    by_feature: Record<string, { calls: number; failed: number; median_latency_ms: number | null }>;
  };
  log: {
    student_id: string;
    name: string;
    concept_id: string;
    concept_name: string;
    hobby: string;
    emoji: string;
    status: "ready" | "failed" | "no_fit" | "error";
    outcome: string;
    attempts: number;
    model: string | null;
    created_at: string;
    hidden: boolean;
    reported: boolean;
    trail: DecisionTrailStep[];
  }[];
}

export function getClassAiDecisions(classId: string): Promise<AiDecisions> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/ai-decisions`);
}

export function getClassPlan(classId: string): Promise<ClassPlan | null> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/plan`);
}

// Coaching notes: a short, privacy-safe note per student for the teacher (AI first, rules as the fallback).
export interface CoachingNote {
  student_id: string;
  name: string;
  alias: string;
  note: string;
  evidence: string[];
  next_step: string;
  source: "ai" | "rules";
}

export interface CoachingRun {
  run_id: number;
  created_at: string;
  source: "agent" | "mixed" | "rules";
  model: string | null;
  note: string | null;
  students: CoachingNote[];
  reused?: boolean;
}

export function getCoachingNotes(classId: string): Promise<CoachingRun | null> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/coaching`);
}

export function generateCoachingNotes(classId: string): Promise<CoachingRun> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/coaching`, {
    method: "POST",
    timeoutMs: LIVE_TIMEOUT_MS, // live model calls, in batches
  });
}

export interface AiStatus {
  configured: boolean;
  up: boolean;
  model: string | null;
  primary: string | null;
  on_fallback: boolean;
  latency_ms: number | null;
}

export function getAiStatus(): Promise<AiStatus> {
  return request("/api/teacher/ai-status");
}

export interface PlanProgress {
  running: boolean;
  stage: string;
  steps: { summary: string; ok: boolean }[];
}

// What the assistant is doing right now; poll while generateClassPlan runs.
export function getClassPlanProgress(classId: string): Promise<PlanProgress> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/plan/progress`);
}

export function generateClassPlan(classId: string): Promise<ClassPlan> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/plan`, {
    method: "POST",
    timeoutMs: LIVE_TIMEOUT_MS, // a live, multi-step model run
  });
}

// ---------------------------------------------------------------------------
// Curriculum (public — the signup page needs interests before anyone logs in)
// ---------------------------------------------------------------------------
export interface Chapter {
  id: string;
  name: string;
  unit_id: string;
  unit_name: string;
  grade: number; // 11 or 12
  domain: string;
  concept_count: number;
  // Present when asked for an interest: concepts with a lesson in it so far.
  lessons_ready?: number;
}

export function getChapters(interest?: string): Promise<Chapter[]> {
  return request("/api/chapters", { query: { interest } });
}

export interface Interest {
  id: string;
  label: string;
  emoji: string;
  description: string;
  status: string;
  chapters_ready: number; // chapters with lessons written so far
  chapters_total: number; // chapters in the agreed scope
}

export function getInterests(): Promise<Interest[]> {
  return request("/api/interests");
}

// ---------------------------------------------------------------------------
// One concept on the roadmap, as returned by GET /api/roadmap.
// ---------------------------------------------------------------------------
// Nothing is ever locked — prerequisites are hints (see missing_prerequisites).
export type ConceptStatus = "mastered" | "available";

export interface RoadmapConcept {
  concept_id: string;
  name: string;
  order: number;
  status: ConceptStatus;
  progress_status: string;
  best_score: number;
  attempts: number;
  missing_prerequisites: string[]; // uncleared prerequisites — a "brush up first" hint
  has_lesson?: boolean; // false = not written yet for the student's interest
  // Personalisation: "known" (the starting check says so), "focus" (a mix-up
  // was seen), or null; a student-facing note; and whether "Continue" opens it.
  personal?: "known" | "focus" | null;
  personal_note?: string | null;
  recommended?: boolean;
  // Concepts inside a chapter open in order. `locked_reason` says what to finish first.
  locked?: boolean;
  locked_reason?: string | null;
}

// ---------------------------------------------------------------------------
// The starting check (after signup) and the learning plan built from it.
// ---------------------------------------------------------------------------
export interface DiagnosticQuestion {
  concept_id: string;
  concept_name: string;
  chapter_name: string | null;
  question: string; // markdown
  options: Record<string, string>; // never the answer
}

export interface HobbyOption {
  id: string;
  label: string;
  emoji: string;
}

export interface DiagnosticResult {
  asked: number;
  known: number;
  mix_ups: number;
  unsure: number;
}

export interface Diagnostic {
  taken: boolean;
  completed_at: string | null;
  hobbies: string[];
  hobby_options: HobbyOption[];
  questions?: DiagnosticQuestion[]; // until taken
  result?: DiagnosticResult; // once taken
}

export interface FocusItem {
  concept_id: string;
  concept_name: string;
  chapter_id: string;
  chapter_name: string | null;
  note: string; // "You might think …"
  source: "check" | "lesson";
  has_lesson: boolean;
}

export interface LearningPlan {
  check: DiagnosticResult & { taken: boolean; completed_at: string | null };
  focus: FocusItem[];
  known: { concept_id: string; concept_name: string }[];
  start: { chapter_id: string; chapter_name: string; reason: string } | null;
  hobbies: string[];
}

export function getDiagnostic(): Promise<Diagnostic> {
  return request("/api/diagnostic");
}

// answers: {concept_id: "A".."D" | "unsure"}; anything left out counts as unsure.
// confidence: {concept_id: "sure" | "think" | "guess"} for picked options.
export function submitDiagnostic(
  answers: Record<string, string>,
  hobbies: string[],
  confidence: Record<string, Confidence> = {},
): Promise<{ result: DiagnosticResult; plan: LearningPlan }> {
  return request("/api/diagnostic", { method: "POST", body: { answers, hobbies, confidence } });
}

export function getLearningPlan(): Promise<LearningPlan> {
  return request("/api/learning-plan");
}

// ---------------------------------------------------------------------------
// The end check: the starting check's concepts again, with parallel questions,
// once the teacher opens it. Compared with the starting check: before → after.
// ---------------------------------------------------------------------------
export type CheckOutcome = "right" | "mix_up" | "unsure";
export type CheckTally = Record<CheckOutcome, number>;

export interface CheckComparison {
  paired: number;
  before: CheckTally;
  after: CheckTally;
  fixed: number; // mix-up → right
  learned: number; // not sure → right
  slipped: number; // right → not right
  concepts: {
    concept_id: string;
    concept_name: string;
    before: CheckOutcome;
    after: CheckOutcome;
    studied: boolean;
  }[];
}

export interface EndCheck {
  status: "not_open" | "needs_start" | "open" | "taken";
  completed_at: string | null;
  questions?: DiagnosticQuestion[]; // when open
  comparison?: CheckComparison; // when taken
}

export function getEndCheck(): Promise<EndCheck> {
  return request("/api/end-check");
}

// answers: {concept_id: "A".."D" | "unsure"}; anything left out counts as unsure.
export function submitEndCheck(
  answers: Record<string, string>,
  confidence: Record<string, Confidence> = {},
): Promise<EndCheck> {
  return request("/api/end-check", { method: "POST", body: { answers, confidence } });
}

// ---------------------------------------------------------------------------
// "My mix-ups": every misconception the student has shown, and its status.
// fixed = right on a different question; recheck = right only on the same
// question after the explanation; active = nothing right since.
// ---------------------------------------------------------------------------
export type MixUpStatus = "active" | "recheck" | "fixed";
export type CheckSource = "start" | "lesson" | "end" | "review";

export interface MixUp {
  concept_id: string;
  concept_name: string;
  chapter_id: string;
  chapter_name: string | null;
  note: string; // "You might think …"
  status: MixUpStatus;
  sure: boolean; // they were sure when they got it wrong
  times: number;
  found_in: CheckSource;
  found_at: string;
  fixed_in: CheckSource | null;
  fixed_at: string | null;
  has_lesson: boolean;
}

export interface MixUps {
  summary: Record<MixUpStatus, number>;
  items: MixUp[];
}

export function getMixUps(): Promise<MixUps> {
  return request("/api/mix-ups");
}

// ---------------------------------------------------------------------------
// Revision: concepts answered right once (cleared, not mastered) get a FRESH
// question — another interest's lesson check — about a day later. Right on it
// = mastered. Nothing is locked: a concept that isn't due can still be tried.
// ---------------------------------------------------------------------------
export interface RevisionItem {
  concept_id: string;
  concept_name: string;
  chapter_id: string;
  chapter_name: string | null;
  reason: string;
  due_at: string;
  due: boolean;
}

export interface Revision {
  due: RevisionItem[];
  later: RevisionItem[];
  no_fresh_question: number;
}

export interface RevisionResult {
  concept_id: string;
  correct: boolean;
  selected_option: string;
  correct_option: string;
  feedback: string; // markdown
  mastery_signal: "mastered" | "partial" | "not_yet";
  mastery_note: string | null;
}

export function getRevision(): Promise<Revision> {
  return request("/api/revision");
}

export function getRevisionQuestion(conceptId: string): Promise<DiagnosticQuestion> {
  return request("/api/revision/question", { query: { concept_id: conceptId } });
}

export function submitRevision(
  conceptId: string,
  answer: string,
  confidence?: Confidence,
): Promise<RevisionResult> {
  return request("/api/revision", {
    method: "POST",
    body: { concept_id: conceptId, answer, confidence: confidence ?? null },
  });
}

// Rates are 0–1, or null when there is nothing to divide.
export interface CheckGains {
  students_started: number;
  students_finished: number;
  paired_answers: number;
  before: CheckTally;
  after: CheckTally;
  right_before: number | null;
  right_after: number | null;
  fixed: number;
  learned: number;
  slipped: number;
  studied: { pairs: number; right_before: number | null; right_after: number | null };
  not_studied: { pairs: number; right_before: number | null; right_after: number | null };
  concepts: {
    concept_id: string;
    concept_name: string;
    chapter_name: string | null;
    students: number;
    right_before: number | null;
    right_after: number | null;
    fixed: number;
  }[];
}

export interface ClassChecks {
  class: ClassSummary;
  open: boolean;
  opened_at: string | null;
  summary: CheckGains;
  students: {
    student_id: string;
    name: string;
    username: string;
    started: boolean;
    finished: boolean;
    before: CheckTally | null;
    after: CheckTally | null;
    fixed: number | null;
    slipped: number | null;
  }[];
}

export function getClassChecks(classId: string): Promise<ClassChecks> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/checks`);
}

export function setClassEndCheck(classId: string, open: boolean): Promise<ClassChecks> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/end-check`, {
    method: "POST",
    body: { open },
  });
}

export function getRoadmap(chapterId: string): Promise<RoadmapConcept[]> {
  return request("/api/roadmap", { query: { chapter_id: chapterId } });
}

// ---------------------------------------------------------------------------
// A lesson's content (the pre-generated, polished markdown).
// ---------------------------------------------------------------------------
// One "## heading" block of an authored lesson, so the page can decide what to
// show and what to tuck behind a click.
export interface LessonSection {
  heading: string;
  markdown: string;
}

// The check question as the browser is allowed to see it: the question and the
// options, never the answer key. Grading happens on the server.
export interface LessonCheck {
  question: string;
  options: Record<string, string>; // {"A": "...", "B": "...", ...}
}

export interface Lesson {
  concept_id: string;
  interest: string;
  body: string; // markdown — the whole lesson (legacy shape)
  worked_example: string; // markdown (legacy, empty for authored lessons)
  check_question: string; // markdown / text (legacy)
  metadata: Record<string, unknown>;
  // Present for authored lessons (everything written since 2026-09):
  title?: string;
  sections?: LessonSection[];
  check?: LessonCheck;
  personal_story?: PersonalStory;
}

// A story written for the student's hobby by the story agent and checked by
// the critic agent. "pending" = being written (poll getPersonalStory);
// "none" = show the lesson's own story as usual.
export type PersonalStory =
  | {
      status: "ready";
      hobby: string;
      emoji: string;
      story: string;
      analogy: string;
      limit: string;
    }
  | { status: "pending"; hobby: string; emoji: string }
  | { status: "none" };

export function getPersonalStory(conceptId: string): Promise<PersonalStory> {
  return request("/api/personal-story", { query: { concept_id: conceptId } });
}

// Fixed reasons only: no free text from a child is stored.
export type StoryReportReason = "wrong_physics" | "confusing" | "not_appropriate" | "other";

export function reportPersonalStory(conceptId: string, reason: StoryReportReason): Promise<unknown> {
  return request("/api/personal-story/report", {
    method: "POST",
    body: { concept_id: conceptId, reason },
  });
}

// ---- Teachers: the AI-written stories in a class -----------------------------
export interface ClassStory {
  student_id: string;
  name: string;
  username: string;
  concept_id: string;
  concept_name: string;
  chapter_name: string | null;
  hobby: string;
  emoji: string;
  story: string;
  analogy: string;
  limit: string;
  model: string | null;
  created_at: string;
  hidden: boolean;
  hidden_by: "student" | "teacher" | null;
  report_reason: StoryReportReason | null;
  report_label: string | null;
  reported_at: string | null;
}

export interface ClassStories {
  summary: {
    written: number;
    showing: number;
    reported: number;
    hidden_by_teacher: number;
    not_written: number; // failed the checks or no hobby fit: the reviewed story was shown
  };
  stories: ClassStory[];
}

export function getClassStories(classId: string): Promise<ClassStories> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/stories`);
}

export function setStoryHidden(studentId: string, conceptId: string, hidden: boolean): Promise<unknown> {
  return request(
    `/api/teacher/stories/${encodeURIComponent(studentId)}/${encodeURIComponent(conceptId)}/visibility`,
    { method: "POST", body: { hidden } },
  );
}

export type LessonStatus =
  | "new"
  | "review"
  | "done"
  | "blocked"
  | "lesson_missing";

// The "envelope" get_next_lesson returns: it always has a status + reason, and
// a lesson only when there's something to teach (lesson is null otherwise).
export interface NextLesson {
  status: LessonStatus;
  reason: string;
  concept_id: string | null;
  concept_name: string | null;
  lesson: Lesson | null;
  prefs?: LessonPrefs; // how this student likes lessons shaped (from the survey)
}

// Presentation only: nothing is hidden or locked.
export interface LessonPrefs {
  mode: "steps" | "all"; // one idea at a time, or everything on one page
  break_after_minutes: number | null; // a gentle stretch nudge after this much reading
  example_first: boolean; // "Try an example" before "The idea"
  gentle: boolean; // physics makes them nervous: be kind about it
}

// conceptId is optional: pass it to open a specific concept instead of the
// engine's pick.
export function getNextLesson(chapterId: string, conceptId?: string): Promise<NextLesson> {
  return request("/api/next-lesson", { query: { chapter_id: chapterId, concept_id: conceptId } });
}

// ---------------------------------------------------------------------------
// Pilot metrics: a lesson view (opened, then reading time) and a 👍/👎.
// ---------------------------------------------------------------------------
export type LessonRating = 1 | -1 | 0; // helpful, not helpful, none

export interface LessonView {
  view_id: string;
  concept_id: string;
  interest: string;
  rating: LessonRating; // the student's current rating of this lesson
}

export function startLessonView(conceptId: string): Promise<LessonView> {
  return request("/api/lesson-views", { method: "POST", body: { concept_id: conceptId } });
}

// Fire-and-forget: report the running total of active seconds on a view.
// Not routed through request(): it must still be delivered while the page is
// closing (keepalive), and a failure here is never worth showing anyone.
// text/plain keeps it a "simple" cross-origin request — no CORS preflight,
// which a closing page wouldn't wait for. The API parses the JSON itself.
export function reportLessonTime(viewId: string, activeSeconds: number): void {
  fetch(`${API_URL}/api/lesson-views/${encodeURIComponent(viewId)}/time`, {
    method: "POST",
    credentials: "include",
    keepalive: true,
    headers: { "Content-Type": "text/plain" },
    body: JSON.stringify({ active_seconds: activeSeconds }),
  }).catch(() => {});
}

export function rateLesson(conceptId: string, rating: LessonRating): Promise<unknown> {
  return request("/api/lesson-ratings", {
    method: "POST",
    body: { concept_id: conceptId, rating },
  });
}

// ---------------------------------------------------------------------------
// POST /api/help — a live, grounded answer. The ONE expensive call: it runs real
// LLM work on the server, so the UI must show a "thinking" state.
// ---------------------------------------------------------------------------
export interface HelpResponse {
  concept_id: string;
  concept_name: string;
  answer: string; // markdown
  verdict: string;
  attempts: number;
}

export function askHelp(conceptId: string, question: string): Promise<HelpResponse> {
  return request("/api/help", {
    method: "POST",
    body: { concept_id: conceptId, question },
    timeoutMs: LIVE_TIMEOUT_MS,
  });
}

// ---------------------------------------------------------------------------
// POST /api/assessment — grade the answer and update mastery in the store,
// the single source of truth the roadmap reads from.
// ---------------------------------------------------------------------------
export interface MasteryRow {
  status: string;
  best_score: number;
  attempts: number;
  [key: string]: unknown;
}

export interface AssessmentResult {
  concept_id: string;
  score: number; // 0-3
  mastery_signal: "mastered" | "partial" | "not_yet";
  feedback: string;
  missing_concepts: string[];
  graded_question: string;
  mastery: MasteryRow;
  // Multiple-choice grading only (authored lessons); absent for legacy lessons.
  attempt_no?: number; // 1 = the student's first pick on this concept
  correct?: boolean;
  selected_option?: string;
  correct_option?: string;
  confidence?: Confidence | null;
  // Mastery needs two DIFFERENT questions right; this says where the student
  // stands ("One more right answer, on a different question, masters it.").
  mastery_note?: string | null;
}

// "How sure are you?" — asked after picking an option in any check.
export type Confidence = "sure" | "think" | "guess";

// `answer` is the chosen option letter ("A".."D") for authored lessons, or free
// text for the older generated ones. Multiple-choice grading is a lookup against
// the lesson file, so it answers immediately — no model call.
export function submitAssessment(
  conceptId: string,
  answer: string,
  confidence?: Confidence,
): Promise<AssessmentResult> {
  return request("/api/assessment", {
    method: "POST",
    body: { concept_id: conceptId, answer, confidence: confidence ?? null },
    timeoutMs: LIVE_TIMEOUT_MS, // legacy free-text grading is still a live call
  });
}


// ---------------------------------------------------------------------------
// "Getting to know you": the survey every student answers on first login.
// Fixed options only (no free text about a child); every question may be skipped.
// ---------------------------------------------------------------------------
export interface SurveyOption {
  id: string;
  label: string;
  emoji?: string;
}

export interface SurveySection {
  id: string;
  title: string;
  emoji: string;
}

export interface SurveyQuestion {
  id: string;
  section: string;
  type: "hobbies" | "hobby_single" | "hobby_multi" | "single" | "multi";
  prompt: string; // hobby questions contain "{hobby}"
  help?: string;
  options?: SurveyOption[];
  max?: number;
}

export interface SurveyTraits {
  hobbies: string[];
  hobby_levels: Record<string, { level: "novice" | "fan" | "player" | "expert"; depth: number | null; knows: number }>;
  focus: { span: "short" | "medium" | "long"; session_minutes: number | null; drift: string | null; distractions: string[] };
  learning: { first_step: string | null; pace: string | null };
  physics: { feel: string | null; maths: string | null; trips: string | null; goal: string | null };
  summary: string[];
}

export interface Survey {
  taken: boolean;
  completed_at: string | null;
  // until taken:
  sections?: SurveySection[];
  questions?: SurveyQuestion[];
  hobby_options?: HobbyOption[];
  hobbies?: string[];
  // once taken (the questions above are always sent, so a form can be shown to edit):
  traits?: SurveyTraits;
  answers?: SurveyAnswers; // their current answers, to prefill the form
  updated_at?: string | null; // set once they've changed their answers
  revision?: number;
}

// One entry per question id: a string, a list, or {hobby: string | string[]}.
export type SurveyAnswers = Record<string, string | string[] | Record<string, string | string[]>>;

export function getSurvey(): Promise<Survey> {
  return request("/api/survey");
}

export function submitSurvey(answers: SurveyAnswers): Promise<Survey> {
  return request("/api/survey", { method: "POST", body: { answers } });
}

// Replace your answers. The old set is kept server-side as history; the teacher sees only this one.
export function updateSurvey(answers: SurveyAnswers): Promise<Survey> {
  return request("/api/survey", { method: "PUT", body: { answers } });
}

// ---------------------------------------------------------------------------
// Teacher: what each student said about themselves, next to how they actually read.
// ---------------------------------------------------------------------------
export interface ClassProfileStudent {
  student_id: string;
  name: string;
  taken: boolean;
  summary: string[]; // plain-English lines
  focus_span: "short" | "medium" | "long" | null;
  hobby_level: "novice" | "fan" | "player" | "expert" | null;
  observed: { views: number; median_minutes: number | null; skim_share: number | null };
  updated_at?: string | null; // set when the student has changed their answers since
}

export interface ClassProfiles {
  summary: {
    taken: number;
    total: number;
    focus: Record<"short" | "medium" | "long", number>;
    pace: Record<string, number>;
    physics_feel: Record<string, number>;
    hobby_level: Record<"novice" | "fan" | "player" | "expert", number>;
  };
  students: ClassProfileStudent[];
}

export function getClassProfiles(classId: string): Promise<ClassProfiles> {
  return request(`/api/teacher/classes/${encodeURIComponent(classId)}/profiles`);
}
