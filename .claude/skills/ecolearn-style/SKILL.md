---
name: ecolearn-style
description: The EcoLearn visual and interaction style ("warm field notes, modern club-room energy"), taken from the Replit design. Use it whenever you build, restyle or review ANY EcoLearn web screen or component (student, teacher, auth, landing, lesson, check, roadmap, dashboards, dialogs, empty/loading/error states) so the whole product looks and feels like one thing.
---

# EcoLearn style

The Replit prototype (`EcoLearn-Physics-Tutor.zip`, app `artifacts/ecolearn`) is the **approved visual
direction for the entire product** (user decision, 2026-10-08). This skill is its distilled, reusable
form. Anything you build in `apps/web/` must be indistinguishable in style from it.

> The Replit app ran on **mock data**. Take its *look and behaviour*, never its data layer. Real screens
> keep calling `apps/web/lib/api.ts` → FastAPI → `src/ecolearn/platform_api.py` (AGENTS.md non-negotiable 1).

## How to use this skill

1. Read this file fully (tokens, rules, recipes, screen blueprints).
2. Open the matching reference in `reference/` **before writing** — copy structure and class names from it:
   | You are building | Open |
   |---|---|
   | Tokens, buttons, inputs, surfaces, top bar, landing, auth, roadmap, start check | `reference/css/base-and-shell.css` |
   | Every screen-specific class (lesson, mix-ups, review, end check, settings, teacher) | `reference/css/screens.css` |
   | Shared building blocks | `reference/components/ui-kit.tsx` |
   | Student screens: landing, auth, starting check, roadmap, mix-ups, settings | `reference/components/student-screens.tsx` |
   | Lesson, review, end check | `reference/components/study-screens.tsx` |
   | Teacher home + class dashboard | `reference/components/teacher-screens.tsx` |
   | Page wiring / providers | `reference/components/experience.tsx`, `root-layout.tsx` |
3. Build with the **existing classes and tokens**; add new ones in the same idiom (below). Don't invent
   a parallel look.
4. Run the checklist at the bottom before calling it done.

## The feeling

Calm, warm, a little playful. Like a well-kept field-notes notebook that a sports club would pin up:
paper-cream surfaces, deep forest green, gold/peach/lavender accents, soft shadows, chunky "pressable"
buttons, generous radii, small uppercase "eyebrow" labels over big tight display headings. Encouraging
copy ("A small step forward", "Good try. You're learning exactly where to look."), never scolding.
Never neon, never glassy, never dense enterprise-grey.

## Design tokens (source of truth: top of `base-and-shell.css`)

Light is `:root`; dark is `.dark` on `<html>` (**dark is the default**, `className="dark"` in the root layout).

| Token | Light | Dark | Use |
|---|---|---|---|
| `--background` | `#f4f3ed` | `#17231f` | page |
| `--surface` | `#fffef9` | `#202e29` | cards, inputs |
| `--surface-soft` | `#ebeae1` | `#293a33` | tracks, chips, quiet fills |
| `--ink` | `#202a27` | `#f1f2e7` | text |
| `--muted` | `#747c73` | `#a2aea4` | secondary text |
| `--line` | `#dedfd4` | `#394940` | borders |
| `--brand` / `--brand-dark` | `#26745d` / `#1b5b48` | `#79c29b` / `#a5d7b6` | primary green |
| `--lime` `--orange` `--gold` | `#d4ef7a` `#e99b61` `#e6bd4d` | same | accents |
| `--danger` | `#bd594e` | `#f18579` | errors |
| `--shadow` | `0 16px 48px rgba(51,67,51,.08)` | `…rgba(0,0,0,.18)` | cards |

- **Fonts:** system stacks only, no web fonts. Display `'Trebuchet MS','Avenir Next',sans-serif`
  (`.display`, letter-spacing `-.045em`); body `'Avenir Next','Trebuchet MS',sans-serif`, 15px.
- **Per-interest accent:** `document.documentElement.dataset.interest = profile.interest` re-themes
  `--brand` / `--brand-dark` (cricket `#bd853c`, football `#4f8b5c`, gaming `#8763b0`, smartphones
  `#4e8e9b`, motorsport `#c76b4d`). Everything uses `var(--brand)`, so one attribute re-skins the app.
  Interest chip colours (`interestsUI` in `ui-kit.tsx`): `#efb45b #84be89 #bd9ce2 #78b9c7 #eb9170`.
- **Tints** are made with `color-mix(in srgb, var(--brand) 8%, var(--surface))`. Selected/hover/active
  states are *always* a brand-tinted surface + brand border, never a new colour.
- **Pastel feature fills** (icon tiles, banners) come in pairs, light and dark: sage `#e3ecdd`/`#2a4033`,
  sand `#f5edda`/`#403b2a`, peach `#f5e6dc`, lavender `#ebe3f2`, sky `#d9eaf0`. A new pastel needs a
  `.dark` twin.
- **Radii:** cards 22px (18px on mobile), controls 12–13px, chips/pills 999px, icon tiles 9–18px.
  **Spacing:** page shell `30px 32px 80px` (mobile `22px 16px 92px`), max width 1200px.

## Component recipes (build blocks live in `ui-kit.tsx` — reuse, don't re-implement)

- **`.surface` / `<Panel>`** – bordered cream card, 22px radius, soft shadow, `padding:22px`.
- **`.button`** – 46px, brand fill, white text (dark: `#14241c`), 13px radius, a **hard 5px under-shadow**
  that collapses on `:active` (`translateY(2px)`); hover lifts 2px. Variants: `.secondary` (surface +
  line border), `.ghost` (transparent, muted). Icon + label with `<ArrowRight size={16}/>` after the text.
- **`.input`** 48px, 12px radius, surface bg. Labels are 12px/700 above, grouped in `display:grid;gap:7px`.
- **`.tag` / `<Pill>`** – 12px/600 outlined pill. **`.eyebrow`** – 11px/700 uppercase, `.12em`, brand colour,
  sits above every `h1/h2`.
- **`<PageHeading eyebrow title description action>`** – every page starts with it (fade-up).
- **`<Meter>`** (`.progress-track/.progress-fill`) 9px rounded bar; thin 5px variant in lesson/summary bars.
- **`<ChoiceButton letter>`** – answer options: lettered square, brand-tinted when selected, ✓ at the end.
  Then the confidence row ("Sure / Think so / Guess") appears under the answers.
- **`<EmptyState>`** – dashed border, ✳ spark, short friendly line, one CTA. **`<Skeleton>`** for loading.
  Never leave a blank screen: every page has loading, empty, error.
- **`<InterestMark>`** – emoji in a tinted rounded tile.
- **App frame:** 72px top bar (logo lockup `e` mark + `ecolearn.`, nav links, theme toggle, avatar);
  **bottom mobile nav** replaces the desktop nav under 768px. Teacher link sits at the end in brand colour.
- **Card hover:** `.card-hover` = lift 3px + brand-tinted border.
- **Decor:** `✳` as a quiet motif; dashed dotted-grid "map" backgrounds; a hero card with orbit rings.
  Keep decoration low-contrast and `aria-hidden`.
- **Maths:** KaTeX (`katex` + `katex/dist/katex.min.css`), `$…$` rendered inline by the `LessonText` helper.
  In `apps/web/` prefer the existing `components/markdown.tsx` pipeline; only the *look* has to match.

## Motion

- Entrances: `.fade-up` (12px rise, .45s). Step changes: framer-motion `AnimatePresence mode="wait"`,
  `opacity 0→1, y 8→0`. Celebrations: the 8-piece `.mastery-confetti` burst (780ms) on *mastered*.
- Wrap the app in `<MotionConfig reducedMotion="user">`; the CSS has a `prefers-reduced-motion` block —
  every new animation must be covered by it.

## Screen blueprints (what each page contains)

| Route | Layout |
|---|---|
| `/` landing | Hero (copy left, orbit-art right) → "Pick your kind of play" 5 interest cards → 4-step "From hmm to got it" → CTA band → footer |
| `/signup` `/login` | Two-column `.auth-wrap`: sage art panel with big mark + equation chip; right: form. Signup is **2 steps** (account → interest/class level) with `AUTH STEP` counter |
| `/start` | Narrow (700px) card flow: hobby chips → 8 questions (progress bar, "not sure" option, "How sure are you?") → plan-result card with score + focus |
| `/roadmap` | Welcome strip with progress ring → chapter select → **zig-zag level map** (nodes: mastered / done / next / locked, cards alternate left–right) + right rail (Continue card, Revise, End check, note) |
| `/lesson` | Top bar (back, `LESSON 01 / 03` + meter) → title → **"Your story"** panel (hobby emoji, analogy, limit note, collapsible original story, report-a-concern select) → section card with dot stepper + Back/Next → worked-example `<details>` → Quick check → rating 👍/👎; sticky outline rail on the right |
| `/mix-ups` | Stat chips (to fix / check again / fixed) → filter tabs → 2-col cards with status colour |
| `/review` | Two-column: copy + concept chip, single revision question |
| `/end-check` | Empty/locked state card, or before→after comparison hero with bars |
| `/settings` | Form panel + aside (class read-only, privacy card, log out) |
| `/teacher` | Class cards grid (3-col), welcome note, create-class dialog (`.modal-backdrop`/`.create-dialog`, credentials shown once) |
| `/teacher/class` | Metric cards (4-col) → chart + misconceptions panel → AI-decisions, checks, stories panels → students table that collapses to cards under 768px |

Breakpoints used: `max-width:900px`, `767px` (mobile: nav moves to the bottom), `390px`. Design phone-first
checks at 375px.

## Porting rules (Replit prototype → this repo)

1. **Data:** never import `mock-data.ts` or use `demo*` fixtures. Call `apps/web/lib/api.ts`. Where the
   backend lacks a field the prototype showed (streaks, XP, lesson images), **omit it or ask** — don't fake it
   (`UI-DATA-GAPS.md` in the zip says the same). Real lesson images exist in this project; show them.
2. **Framework:** `apps/web/` is **Next.js 16** (not the prototype's 15). Read `apps/web/node_modules/next/dist/docs/`
   before touching routing, cookies or error files; `error.tsx` uses `unstable_retry`. Route protection is a
   client guard, not `proxy.ts`. No `wouter`, no Vite.
3. **Styling:** the prototype uses **plain global CSS classes** (Tailwind v4 is only imported for resets),
   not utility classes. Keep that: put tokens/shell in `globals.css` (or imports of it) and screen CSS in a
   `screen-styles.css`-style file. Don't mix in a second system (no per-component Tailwind colour utilities,
   no hard-coded hex outside the token/pastel lists above).
4. **Theme:** use the existing `apps/web/components/theme-toggle.tsx` behaviour (dark / light / device) but with
   these tokens. The prototype's toggle only stores `ecolearn-theme` in localStorage; keep dark as default.
5. **Don't ship the prototype's extras:** `components/ui/*` (shadcn, unused by the screens), `mockup-sandbox`,
   `api-server`, Replit/Vite config, `@replit/*` plugins.
6. **Keep existing behaviour** that the prototype lacks (error/404 pages, toasts, login lockout messages,
   confidence picker states, polling "being written…" story state): restyle, don't remove.
7. **A11y is part of the style:** visible 3px brand focus ring (already global), 44px+ touch targets,
   `aria-label` on icon buttons, `role="status"` on feedback, colour is never the only signal (status has
   icon + text), contrast ≥ 4.5:1 for body text (the tiny 8–10px labels in the prototype are *too small* —
   use ≥ 11px for real content, and verify the muted-on-surface pairs).

## Applying it to a screen (procedure)

1. Find the matching blueprint row and open the reference component + its CSS block (`grep` the class prefix).
2. Re-create the JSX structure with the same class names; wire the real `api.*` calls and real types.
3. Reuse `ui-kit` pieces; if you need a new primitive, add it to the kit in the same style.
4. New CSS: tokens only, `color-mix` for tints, a `.dark` twin for any literal colour, mobile rule at `767px`.
5. Verify in the browser at 1280px and 375px, light and dark, plus the loading / empty / error states.

## Checklist (all must be true)

- [ ] Only token colours (or listed pastels with dark twins); no stray greys/blues/indigo (the old `apps/web/` indigo is being retired).
- [ ] Eyebrow + display heading + muted description on every page via `PageHeading`.
- [ ] Buttons are the pressable `.button` family; one primary per view.
- [ ] Cards are `.surface` (22px radius); selected state = brand tint + brand border.
- [ ] Loading skeleton, empty state, and friendly error state exist.
- [ ] Works at 375px with the bottom nav; no horizontal scroll; tables degrade to cards.
- [ ] Dark mode checked (default) and light mode checked.
- [ ] Reduced-motion respected; focus ring visible; icon buttons labelled.
- [ ] Per-interest accent still works (`data-interest`).
- [ ] No mock data; `tsc --noEmit`, `npm run lint`, `npm run build` clean (stop `next dev` before building).

## Where it lives in `apps/web/` (applied 2026-10-08)

The restyle of the real app is done; extend it, don't redo it.

- `apps/web/app/globals.css` – the shadcn tokens now point at the house palette (`--primary` = `var(--brand)`,
  `--card` = `--surface`, `--muted-foreground` = `--ink-muted`, …), plus the `[data-interest]` accents (lighter in
  dark). `ecolearn.css` is imported `layer(components)` so Tailwind utilities still win over it.
- `apps/web/app/ecolearn.css` – the class-based rules (copy of the reference CSS; `--muted` was renamed `--ink-muted`
  because shadcn owns `--muted`) plus a few additions at the bottom.
- `apps/web/components/ui-kit.tsx` – `PageHeading`, `Panel`, `Pill`, `Meter`, `EmptyState`, `Skeleton`, `InterestMark`.
- shadcn primitives (`ui/button|card|badge|input|progress|dialog`) are restyled in place, so every existing
  `<Button>` / `<Card>` is already on-style: the pressable button, 22px cards.
- `components/site-nav.tsx` is the house top bar + mobile bottom nav; `auth-provider.tsx` sets `data-interest`.
- Student/teacher pages mix house classes (`.surface`, `.eyebrow`, `.display`, `.page-shell`, `.side-action`…) with
  Tailwind utilities on tokens. Both are fine; hard-coded hex is not.
- Sticky bars sit at `bottom-20 md:bottom-3` so they clear the mobile bottom nav.
- Correct/wrong feedback stays semantic green/red (`--success`, `--destructive`), not the interest accent.
- Light-theme interest accents were darkened so white button text is >= 4.5:1.

## Provenance

Extracted 2026-10-08 from `EcoLearn-Physics-Tutor.zip` (Replit project: `artifacts/ecolearn/src/index.css`,
`app/screen-styles.css`, `components/{ui-kit,experience,student-screens,study-screens,teacher-screens}.tsx`).
The `reference/` files are unmodified copies; they are examples to read, not code to import.
