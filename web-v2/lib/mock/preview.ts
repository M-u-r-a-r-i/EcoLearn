// Fictional fixtures for the three design previews (/preview/a, /b, /c).
// Nothing here is real student data. Phase 2 moves screen data behind the
// request() mock layer; the previews only need a small, shared sample.

export type InterestId = "cricket" | "football" | "gaming" | "smartphones" | "motorsport";

export interface InterestInfo {
  id: InterestId;
  label: string;
  emoji: string;
  hue: number; // oklch hue the directions recolour with
  tagline: string;
  story: string; // the reviewed lesson's opening story, in this interest
  personal: string; // the AI-written personal story (labelled in the UI)
  stem: string; // check question stem
}

export const INTERESTS: InterestInfo[] = [
  {
    id: "cricket",
    label: "Cricket",
    emoji: "🏏",
    hue: 25,
    tagline: "Why a soft catch stings less",
    story:
      "A fast bowler sends down a 140 km/h ball. If you stop it dead with stiff hands, it hurts. If you pull your hands back as it lands, it barely stings. Same ball, same speed. What changed?",
    personal:
      "Remember the nets last Sunday, Aarav? You dropped the same catch twice. The second time you gave with the ball and it stayed in your hands. That give is Newton's second law at work.",
    stem: "A fielder pulls their hands back while catching a fast ball. Why does that hurt less?",
  },
  {
    id: "football",
    label: "Football",
    emoji: "⚽",
    hue: 150,
    tagline: "Why a keeper's gloves go back",
    story:
      "A striker hits the ball at 100 km/h straight at the keeper. A keeper who punches it stiffly feels it. One who lets their hands travel back with it keeps hold. Same shot, two feelings.",
    personal:
      "On Saturday you tried to trap a long ball with a stiff foot and it bounced away. Let your foot go back with the ball and it dies at your feet. That is the same idea.",
    stem: "A goalkeeper lets their hands move back as they catch a hard shot. Why does that help?",
  },
  {
    id: "gaming",
    label: "Gaming",
    emoji: "🎮",
    hue: 295,
    tagline: "Why heavy characters turn slowly",
    story:
      "In your favourite game the heavy tank takes ages to turn, while the scout zips about. The engine pushes both with the same strength. So why do they feel so different?",
    personal:
      "You told us you main the slow, armoured hero. Notice how your dodge feels late? The game is quietly doing F = ma, with a big m.",
    stem: "Two game characters get the same push. The heavy one speeds up less. Why?",
  },
  {
    id: "smartphones",
    label: "Smartphones",
    emoji: "📱",
    hue: 235,
    tagline: "Why a case saves your screen",
    story:
      "Drop a phone on tile and the screen cracks. Drop it in a soft case and it survives. The fall is the same, but the stop is slower. Slower stops need less force.",
    personal:
      "You mentioned the cracked corner on your old phone. Without a case, the stop took a blink. With one, it takes a little longer, and that little is everything.",
    stem: "A phone in a rubber case survives a drop that cracks a bare phone. Why?",
  },
  {
    id: "motorsport",
    label: "Motorsport",
    emoji: "🏎️",
    hue: 55,
    tagline: "Why crash barriers are soft",
    story:
      "A racing car hits a wall at 200 km/h. If the wall were solid concrete, the stop would be instant and brutal. Tyre barriers and crumple zones stretch the stop out. The driver walks away.",
    personal:
      "You said you watch every race with your dad. Next time you see a barrier of tyres, you will know it is not for show. It is stretching time.",
    stem: "Race tracks use soft tyre barriers instead of hard walls. What does the soft barrier change?",
  },
];

export const interestById = (id: string): InterestInfo =>
  INTERESTS.find((i) => i.id === id) ?? INTERESTS[0];

export type NodeState = "mastered" | "done" | "next" | "open" | "locked" | "soon";

export interface MockConcept {
  id: string;
  name: string;
  state: NodeState;
  note: string;
  badge?: "known" | "focus";
}

export const CHAPTER = { name: "Laws of Motion", classLevel: "Class 11", pct: { done: 3, mastered: 2, total: 8 } };

export const CONCEPTS: MockConcept[] = [
  { id: "c1", name: "Newton's first law", state: "mastered", note: "Two different questions right. Locked in.", badge: "known" },
  { id: "c2", name: "Inertia and mass", state: "mastered", note: "Two different questions right. Locked in." },
  { id: "c3", name: "Linear momentum", state: "done", note: "Right once. A fresh question comes tomorrow." },
  { id: "c4", name: "Newton's second law", state: "next", note: "Next up. About 6 minutes.", badge: "focus" },
  { id: "c5", name: "Free-body diagrams", state: "open", note: "Open. Try it any time after the second law." },
  { id: "c6", name: "Friction", state: "locked", note: "Finish Free-body diagrams first." },
  { id: "c7", name: "Circular motion", state: "locked", note: "Finish Friction first." },
  { id: "c8", name: "Impulse", state: "soon", note: "Coming soon. We're still writing this one." },
];

export const LESSON_STEPS = ["The story", "The idea", "Worked example", "Where it breaks", "Key takeaway", "Check"] as const;

export const LESSON = {
  title: "Newton's second law",
  idea: "The harder you push, the faster it speeds up. The heavier it is, the less it speeds up. We write that as F = m × a.",
  equation: "F = m a",
  example: {
    prompt: "A 0.16 kg ball arrives at 30 m/s and stops in 0.02 s with stiff hands. How big is the average force?",
    steps: ["a = Δv / Δt = 30 / 0.02 = 1500 m/s²", "F = m a = 0.16 × 1500 = 240 N", "Now stop it in 0.10 s: a = 300 m/s², F = 48 N. Five times less."],
  },
  breaks:
    "The picture \"force is what keeps things moving\" breaks here. A net force changes motion. It does not keep it going. With no net force the ball just carries on.",
  takeaway: "Same change in speed, more time, smaller force.",
};

export const OPTIONS = [
  { key: "A", text: "The ball loses less speed overall", why: "The ball still stops. Its change in speed is the same.", mix: "Mixing up: speed lost vs force felt" },
  { key: "B", text: "The stop takes longer, so the force is smaller", why: "Yes. Same change in speed spread over more time means a smaller average force.", mix: "" },
  { key: "C", text: "The ball is lighter when it moves slowly", why: "Mass doesn't change with speed in everyday physics.", mix: "Mixing up: mass vs weight" },
  { key: "D", text: "Hands absorb the force so it disappears", why: "Forces don't vanish. They get spread over a longer time.", mix: "Mixing up: force is used up" },
] as const;
export const CORRECT = "B";

export const TEACHER = {
  className: "Class 11-B · Physics",
  students: 25,
  tiles: [
    { label: "Starting check", value: "23 of 25", sub: "took it" },
    { label: "End check", value: "20 of 25", sub: "took it" },
    { label: "Right answers", value: "58% → 77%", sub: "start → end" },
    { label: "Mix-ups", value: "54 → 31", sub: "start → end" },
  ],
  compare: [
    { label: "Studied the idea", before: 52, after: 81 },
    { label: "Skipped the idea", before: 55, after: 61 },
  ],
  misconceptions: [
    { name: "Force is used up", count: 11, sure: 6 },
    { name: "Speed lost = force felt", count: 9, sure: 4 },
    { name: "Heavier falls faster", count: 7, sure: 5 },
  ],
  ideas: [
    { name: "Second law", first: 49, students: 22 },
    { name: "Momentum", first: 61, students: 24 },
    { name: "Friction", first: 66, students: 19 },
    { name: "Circular motion", first: 38, students: 12 },
  ],
  plan: [
    "Start with the soft-landing demo: egg drop, three cushions.",
    "Spend 10 minutes on \"force is used up\". 11 students picked it, 6 of them sure.",
    "Move Circular motion to Thursday. Only 12 of 25 have opened it.",
  ],
  ai: { drafts: 40, rule: 5, critic: 3, shown: 32, human: 1 },
  students_list: [
    { name: "Aarav K.", done: 6, mixups: 2 },
    { name: "Meera I.", done: 8, mixups: 0 },
    { name: "Kabir S.", done: 4, mixups: 3 },
    { name: "Diya R.", done: 5, mixups: 1 },
  ],
};
