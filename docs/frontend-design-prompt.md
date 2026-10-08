# Prompt: design EcoLearn's whole frontend (three options, then merge)

Paste everything below the line into a new Claude session opened in `D:\Projects\EcoLearn`
(with your design skill enabled). If that session can't see the repo, attach `web/lib/api.ts`
and `AGENTS.md` and tell it the screens list below is the full scope.

---

You are designing the complete student and teacher frontend of **EcoLearn**, a personalised AI
physics tutor for Class 11/12 students (CBSE/ISC, ages 16-18) in India, being piloted with real
schools in October 2026 and presented at a hackathon final (HackAStone, theme "Agentic AI for
Education", judged on Innovation 30, Technology readiness 20, Commercial viability 15, Education
significance 15, Presentation 10, Demo 10). The UI must look and feel like a product, not a
school website: interactive, game-like, warm, trustworthy. Use your design skill throughout.

## How we will work (three phases, stop after each and wait for me)

**Phase 1 - Three design directions.** Do NOT start by coding everything. First read the repo
(see "Read first"), then propose THREE clearly different visual directions (for example: a
playful game-map style; a calm editorial/notebook style; a bold sports-broadcast style. Choose
your own, but make them genuinely different in layout, type, colour, shape language and motion,
not three palettes of one design). For each: name, one-paragraph rationale for 16-18 year olds,
colour tokens (light AND dark), type pairing (Google Fonts only), radius/shadow/motion language,
and how each of the 5 interests (cricket, football, gaming, smartphones, motorsport) recolours it.
Then build each as a **clickable prototype of these 5 key screens** with mock data:
landing, roadmap, lesson (steps), check (question and result), teacher class dashboard.
Put them at `/preview/a`, `/preview/b`, `/preview/c` inside a COPY of the web app (see
"Where to work"), plus a `/preview` index page that shows all three side by side with a theme
(light/dark) and phone/desktop toggle. Tell me how to run it. **Stop and let me choose.**

**Phase 2 - Build the chosen design across every screen** (full list below), all states
included (loading, empty, error, locked, coming soon, done, mastered). I may ask for changes
or to mix elements from two directions.

**Phase 3 - Merge-ready handover.** Make the result drop into the real app with no backend
change (see "Merge contract"), run the checks, and give me a short merge checklist.

## Where to work

- Work on a new git branch `design/frontend-v2`, and in a copy of the frontend at
  `D:\Projects\EcoLearn\web-v2\` (copy `web/`, keep its `package.json` stack). Never edit `web/`,
  `src/`, `api/`, `tests/` or `data/` during Phases 1-2. Do not commit to `main`. Do not push
  unless I say so.
- Mock data lives behind the existing data layer (see Merge contract), never inside components.

## Read first (do not skip)

1. `AGENTS.md` (project rules and decisions), then `web/AGENTS.md`: **this is Next.js 16, not
   the version you know**. Read the relevant guide in `web/node_modules/next/dist/docs/` before
   touching routing, cookies or error files (`error.tsx` uses `unstable_retry`, not `reset`; route
   protection is a client guard, not `proxy.ts`).
2. `web/lib/api.ts`: the ONLY place the frontend talks to the backend. Every screen's data shape
   is typed there.
3. The current UI, to see what exists and what to keep functionally: `web/app/**`,
   `web/components/**` (notably `roadmap-path.tsx`, `lesson-stepper.tsx`, `check-feedback.tsx`,
   `check-question.tsx`, `personal-story.tsx`, `class-insights.tsx`, `class-checks.tsx`,
   `ai-decisions.tsx`, `teaching-assistant.tsx`), and `web/app/globals.css` (theme tokens).
4. `PROJECT_HISTORY.md` sections 9zr to 9zx (the latest UI decisions and why).

## Stack (fixed, so the result merges)

Next.js 16 App Router, React 19, TypeScript, Tailwind CSS v4 (theme in CSS, `@theme`, no JS
config), shadcn/ui primitives in `components/ui`, `lucide-react` icons, `react-markdown` +
KaTeX for lesson maths. Motion: prefer plain CSS (keyframes in `globals.css`). You may add ONE
animation library (Framer Motion) only if a design truly needs it, and you must say so in the
report. No other new dependencies, no analytics, no trackers, no third-party embeds. Fonts: Google
Fonts via `next/font` only.

## Non-negotiable product rules (design must express these)

- **Accounts are username + password, no email** (users are minors). Never add email, social
  login, phone numbers or avatars with photos.
- **Chapters are never locked; concepts inside a chapter open in order** (locked until the one
  before is done, or the starting check says the student knows it). **Only a teacher moves a
  student between Class 11 and Class 12**: students see only their own class's chapters, and
  Settings shows the class read-only.
- **A concept is "Done" after one right answer and "Mastered" only after two different questions
  right** (the second comes in Review about a day later). The UI must make that road visible
  (Right once -> new question tomorrow -> Mastered).
- **Wrong answers are framed as "what to fix", never as failure.** Each wrong option maps to a
  named misconception; "How sure are you?" (sure / think so / guessing) follows every pick; "I'm
  not sure yet" is always an honest option in checks.
- **Every lesson opens with a story and has images.** Lessons: The story, The idea, Worked example
  (try-first reveal), Where the picture breaks, Key takeaway, then the check. A personal,
  AI-written story for the student's hobby may appear above the reviewed story; it is clearly
  labelled as AI-written and checked, with a "Something wrong with this story?" report button.
- **AI is shown honestly.** Teachers see "How the AI decided" (guardrail counts, a decision log
  with reasons). Never present rule-based features as AI, and never invent numbers.
- Reading level about 16, warm second person ("You might be mixing up..."), short sentences.
- Five interests, each with an emoji and an accent: cricket, football, gaming, smartphones,
  motorsport. The UI recolours to the student's interest.

## Quality bar

Mobile-first (design at 375 px first; many students use phones), 16 px side gutters, no sideways
scroll at 375 px. Dark and light themes plus "same as device"; both must pass WCAG AA contrast.
Fully keyboard-usable with visible focus; screen-reader labels on every icon-only control; colour
is never the only signal (pair with icon or word). `prefers-reduced-motion` disables all
non-essential motion (confetti, pulses, slides). Skeletons for every loading state; friendly empty
and error states that say what to do next. Interactions that make it feel alive: path nodes,
step transitions, option selection, confetti on right answers, count-ups, but never blocking
or slow (nothing over 400 ms except a one-off celebration).

## Screens (all routes; keep these paths)

Student: `/` landing (what it is: physics through cricket, football, gaming, phones or cars;
how it works; log in / sign up) - `/signup` (2 steps: details, then interest and class) -
`/login` - `/start` starting check (intro, hobby tiles, 8 questions with progress, plan reveal) -
`/roadmap?chapter=` level map with progress ring, concept states (Mastered, Done, Next up, Open,
Locked, Coming soon), chapter picker (own class only), revision card, end-check card, learning
plan card - `/lesson?chapter=&concept=` step-by-step lesson with "show everything" mode and the
"I'm stuck" help chat - `/assessment?chapter=&concept=` check question, then result (right: confetti
and the road to mastered; wrong: red/green replay and "Why") - `/mix-ups` (To fix / Check again /
Fixed) - `/review` (revision question) - `/end-check` (questions, then a before -> after result) -
`/settings` (name, interest, read-only class, password).

Teacher: `/teacher/login` - `/teacher` (class list, create a class from pasted names, printable
login slips with passwords shown once) - `/teacher/class?id=` dashboard: tiles (starting check
23 of 25, end check 20 of 25, right answers 58% -> 77%, mix-ups 54 -> 31), studied vs not-studied
comparison, per-idea table, most common misconceptions, Teaching assistant (markdown plan),
personal stories review (hide/restore), "How the AI decided", students table with a Class
dropdown and Reset password - `/teacher/account`.
System: `error.tsx`, `global-error.tsx`, `not-found.tsx`, loading skeletons.

## Merge contract (so I can plug it into the real backend)

1. **`web-v2/lib/api.ts` keeps every exported function name, argument and return type exactly as
   in `web/lib/api.ts`.** Do not rename or reshape. If a design needs data the API doesn't give,
   do NOT invent an endpoint: list it at the end ("data wishes") so I can decide.
2. Add the mock layer INSIDE `request()` in `lib/api.ts`, switched by
   `NEXT_PUBLIC_USE_MOCK=1`, with fixtures in `lib/mock/*.ts` keyed by endpoint path (fictional
   Indian names, no real people, no real data). With the flag unset the app must call the real API
   at `NEXT_PUBLIC_API_URL` (default `http://localhost:8000`) exactly as today (cookie session,
   `credentials: "include"`).
3. Keep route paths, query params (`?chapter=`, `?concept=`, `?id=`) and the client-side auth
   guard as they are. Keep `useChapter`, `useFetch`, `useAuth` semantics.
4. Components are pure presentation over those hooks; no fetching in components except through
   `lib/api.ts`.
5. Phase 3 deliverable: `npx tsc --noEmit`, `npm run lint` and `npm run build` all clean in
   `web-v2`; a `MERGE.md` listing every file to copy into `web/`, any deletes, any new env var
   (should be none beyond the mock flag), and what I should click through to verify; plus the
   "data wishes" list. Do not run `npm run build` while `next dev` is running (both write `.next`).

## Privacy and safety

Use only fictional data. Do not read or print `.env`, `data/progress.db` or any password. Do not
send anything to external services. No tracking pixels, no remote fonts other than `next/font`.

## What I expect back in Phase 1

A short message with: how to run the previews, a table comparing the three directions (mood, best
for, risk), screenshots or the exact URLs to open, and your honest recommendation with reasons.
Then wait for my choice.
