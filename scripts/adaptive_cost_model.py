"""Cost of the adaptive flow: AI writes each lesson from the student's interests AND how they did on the previous lesson,
reusing a lesson whenever an earlier student had the same "key". All inputs are printed; token sizes come from
generation_cost_model.py (measured lesson and prompt sizes; thinking assumed 1x output).

The flow per student:
  step 0  sign-up + survey + starting check  -> one AI call turns the answers into a profile
  step n  lesson n: look up (concept, key); on a miss the AI writes it (writer + critic + answer check, 1.4 rounds)
          the student reads it and answers the check (graded by rules, no AI)
          one AI call updates the profile from that interaction; the new profile decides lesson n+1's key

What decides reuse is the key. Scenarios:
  A  key = main interest (5) + how lesson n-1 went (K buckets)            -> few variants, reuse saturates fast
  B  key = main interest + 2 of 20 hobbies (950 profiles) + K buckets      -> many variants
  C  key = interest profile + the WHOLE history (every past bucket)        -> variants multiply each lesson
Distinct lessons are counted as if keys were equally likely (the most generations for a given number of keys);
real students cluster (most pick cricket), so real reuse is higher than this.
"""
import math

FX = 88
CONCEPTS = 249
MONTHS = 24
K = 4                     # how a lesson went: got it / partly / mix-up / struggled
EXTRAS_MONTH_INR = 3.79   # doubt chat, plans, coaching: measured per student per month

# tokens per call (in, out)
writer = (9000 + 800, 3400)        # guide + brief + gold example + context, plus the learner profile
critic = (4700, 800)
solver = (800, 600)
ROUNDS = 1.4
LESSON_IN = (writer[0] + critic[0] + solver[0]) * ROUNDS
LESSON_OUT = (writer[1] + critic[1] + solver[1]) * ROUNDS
PROFILE_IN, PROFILE_OUT = 2800, 600   # profile + interaction log (time, answers, confidence, chat topics) -> new profile
ONBOARD_IN, ONBOARD_OUT = 1500, 600

models = {
    "Gemini 3.1 Flash-Lite (today)": (0.25, 1.50),
    "Gemini 3.8 Flash (2027 price)": (1.50, 7.50),
    "Gemini 2.5 Pro": (1.25, 10.00),
}


def inr(tin, tout, p):
    return (tin * p[0] + tout * p[1]) / 1e6 * FX


def distinct(variants, n):
    """Expected number of different keys hit when n students each draw one of `variants` equally likely keys."""
    if variants <= 0 or n <= 0:
        return 0.0
    if variants > 1e15:
        return float(n)
    return variants * -math.expm1(n * math.log1p(-1 / variants))


def variants(scenario, lesson_no):
    profiles = {"A": 5, "B": 5 * 190, "C": 5 * 190}[scenario]
    if lesson_no == 1:
        return profiles
    if scenario == "C":
        return profiles * K ** min(lesson_no - 1, 60)
    return profiles * K


def generations(scenario, n):
    return sum(distinct(variants(scenario, i), n) for i in range(1, CONCEPTS + 1))


print(f"per call tokens: lesson (writer+critic+check, x{ROUNDS}) in {LESSON_IN:,.0f} / out {LESSON_OUT:,.0f}; "
      f"profile update in {PROFILE_IN:,} / out {PROFILE_OUT:,}; onboarding in {ONBOARD_IN:,} / out {ONBOARD_OUT:,}\n")

print("STEP COSTS (Rs, one call each)")
for m, p in models.items():
    print(f"  {m:30s} onboarding {inr(ONBOARD_IN, ONBOARD_OUT, p):6.3f} | new lesson {inr(LESSON_IN, LESSON_OUT, p):6.2f} | "
          f"reused lesson 0 | check 0 (rules) | profile update {inr(PROFILE_IN, PROFILE_OUT, p):6.3f}")

print("\nPER STUDENT, NO REUSE AT ALL (2 years, 249 lessons)")
for m, p in models.items():
    fixed = inr(ONBOARD_IN, ONBOARD_OUT, p) + CONCEPTS * inr(PROFILE_IN, PROFILE_OUT, p)
    gen = CONCEPTS * inr(LESSON_IN, LESSON_OUT, p)
    print(f"  {m:30s} lessons Rs {gen:7,.0f} + profiling Rs {fixed:5,.0f} + extras Rs {EXTRAS_MONTH_INR*MONTHS:.0f}")

print(f"\nREUSE AND SCALE (2-year totals; K = {K} outcome buckets)")
p = models["Gemini 3.1 Flash-Lite (today)"]
p_pro = models["Gemini 2.5 Pro"]
for sc in "ABC":
    print(f"\n  Scenario {sc}: variants for lesson 1 = {variants(sc,1):,}, lesson 2 = {variants(sc,2):,}, lesson 5 = {variants(sc,5):,.0f}")
    print(f"    {'students':>10} {'lessons written':>16} {'reused':>7} {'Rs/student FL':>14} {'total FL (Rs lakh)':>19} {'Rs/student Pro':>15}")
    for n in (1, 100, 1_000, 10_000, 100_000, 1_000_000):
        g = generations(sc, n)
        served = n * CONCEPTS
        per_student_fixed = inr(ONBOARD_IN, ONBOARD_OUT, p) + CONCEPTS * inr(PROFILE_IN, PROFILE_OUT, p) + EXTRAS_MONTH_INR * MONTHS
        per_student_fixed_pro = inr(ONBOARD_IN, ONBOARD_OUT, p_pro) + CONCEPTS * inr(PROFILE_IN, PROFILE_OUT, p_pro) + EXTRAS_MONTH_INR * MONTHS
        total = g * inr(LESSON_IN, LESSON_OUT, p) + n * per_student_fixed
        total_pro = g * inr(LESSON_IN, LESSON_OUT, p_pro) + n * per_student_fixed_pro
        print(f"    {n:>10,} {g:>16,.0f} {1 - g/served:>7.1%} {total/n:>14,.0f} {total/1e5:>19,.2f} {total_pro/n:>15,.0f}")

print("\nWHEN DOES REUSE STOP IN SCENARIO C (the first lesson where most students get a lesson nobody had before)")
for n in (1_000, 100_000, 1_000_000):
    for i in range(1, CONCEPTS + 1):
        if distinct(variants("C", i), n) / n > 0.5:
            print(f"  {n:>9,} students: from lesson {i} on, over half of lessons are written fresh")
            break
