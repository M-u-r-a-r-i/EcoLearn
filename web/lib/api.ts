// Typed client for the EcoLearn FastAPI backend.
//
// Every call to the backend goes through a function here, so the rest of the app
// never writes raw fetch() calls or hardcodes URLs. This mirrors the Python side:
// the UI talks to ONE module, and that module talks to the network.

// The base URL comes from the environment (web/.env.local). We fall back to
// localhost so the app still runs if the var is missing in development.
const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

// ---------------------------------------------------------------------------
// Types — describe the shapes that cross the network, so TypeScript can check
// our usage. These match what FastAPI returns (api/main.py) / accepts.
// ---------------------------------------------------------------------------
export interface StudentProfile {
  student_id: string;
  name: string;
  interest: string;
  level: string;
  created_at: string;
}

export interface CreateStudentInput {
  name: string;
  interest: string;
  level: string;
}

// ---------------------------------------------------------------------------
// POST /api/student  ->  create (or load) a student, return their profile.
// ---------------------------------------------------------------------------
export async function createStudent(
  input: CreateStudentInput,
): Promise<StudentProfile> {
  // fetch() sends the HTTP request. We POST JSON, so we set the method, the
  // Content-Type header, and stringify the body.
  const response = await fetch(`${API_URL}/api/student`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  });

  // fetch() does NOT throw on HTTP error codes (404/500) — only on network
  // failures (backend down, DNS, CORS block). So we check `response.ok`
  // (true for 2xx) ourselves and turn a bad status into an error.
  if (!response.ok) {
    throw new Error(`Backend returned ${response.status} ${response.statusText}`);
  }

  // Parse the JSON body into a typed StudentProfile.
  return (await response.json()) as StudentProfile;
}

// ---------------------------------------------------------------------------
// One concept on the roadmap, as returned by GET /api/roadmap.
// ---------------------------------------------------------------------------
export type ConceptStatus = "mastered" | "available" | "locked";

export interface RoadmapConcept {
  concept_id: string;
  name: string;
  order: number;
  status: ConceptStatus;
  progress_status: string;
  best_score: number;
  attempts: number;
  missing_prerequisites: string[];
}

// ---------------------------------------------------------------------------
// GET /api/roadmap?student_id=...&chapter_id=...  ->  the chapter's concepts.
//
// This is a GET (it only reads), so the inputs ride in the URL as query params
// rather than in a body. We build the URL with URLSearchParams so values are
// safely encoded.
// ---------------------------------------------------------------------------
export async function getRoadmap(
  studentId: string,
  chapterId: string,
): Promise<RoadmapConcept[]> {
  const url = new URL(`${API_URL}/api/roadmap`);
  url.searchParams.set("student_id", studentId);
  url.searchParams.set("chapter_id", chapterId);

  const response = await fetch(url, { method: "GET" });
  if (!response.ok) {
    throw new Error(`Backend returned ${response.status} ${response.statusText}`);
  }
  return (await response.json()) as RoadmapConcept[];
}
