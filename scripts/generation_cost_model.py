"""Cost of generating the whole syllabus per student vs EcoLearn's shared library. All inputs printed."""
FX = 88
CONCEPTS = 249            # full Class 11 + 12 syllabus, both boards
FORMATS = 3               # explain, challenge, misconception
INTERESTS = 5
MONTHS = 24               # Class 11 + 12

# Tokens per lesson attempt (measured sizes; thinking assumed equal to visible output)
LESSON_OUT = 1700         # 6,434 chars mean / ~3.8 chars per token
THINK = 1700              # hidden reasoning, billed as output (assumption: 1x)
GUIDE_IN = 5700 + 900 + 1700 + 700   # authoring guide + brief + one gold example + concept and student context
writer = (GUIDE_IN, LESSON_OUT + THINK)
critic = (LESSON_OUT + 3000, 400 + 400)    # lesson + checklist and facts in; verdict + reasoning out
solver = (800, 300 + 300)                  # answer-key check, as in Practice with AI
ROUNDS = 1.4              # measured: 2.8 calls per story = writer + critic, 1.4 rounds
tin = (writer[0] + critic[0] + solver[0]) * ROUNDS
tout = (writer[1] + critic[1] + solver[1]) * ROUNDS

models = {
    "Gemini 2.5 Flash-Lite": (0.10, 0.40),
    "Gemini 3.1 Flash-Lite (used today)": (0.25, 1.50),
    "Gemini 3.8 Flash (intro price)": (0.75, 3.75),
    "Gemini 3.8 Flash (from 2027)": (1.50, 7.50),
    "Gemini 2.5 Pro": (1.25, 10.00),
}
EXTRAS_MONTH_INR = 3.79   # measured: stories, plans, coaching, chat per student per month (unit-economics page)

print(f"tokens per lesson (incl. checks and rewrites): in {tin:,.0f}, out {tout:,.0f}")
per_lesson = {m: (tin * p[0] + tout * p[1]) / 1e6 for m, p in models.items()}
for m, usd in per_lesson.items():
    expl = usd * CONCEPTS
    full = expl * FORMATS
    print(f"{m:36s} lesson ${usd:.4f} (Rs {usd*FX:.2f}) | per student explain ${expl:.2f} (Rs {expl*FX:,.0f}) | 3 formats ${full:.2f} (Rs {full*FX:,.0f})")

lib_lessons = CONCEPTS * INTERESTS * FORMATS
print(f"\nshared library: {lib_lessons} lessons")
for m, usd in per_lesson.items():
    print(f"  {m:36s} one-time ${usd*lib_lessons:,.0f} (Rs {usd*lib_lessons*FX:,.0f})")

extras_2y = EXTRAS_MONTH_INR * MONTHS
print(f"\nextras per student over 2 years: Rs {extras_2y:.0f}")
print("\nscale (2-year totals, Rs lakh; 1 crore = 100 lakh)")
for n in (1_000, 10_000, 100_000, 1_000_000):
    ours = (per_lesson["Gemini 2.5 Pro"] * lib_lessons * FX + extras_2y * n) / 1e5
    cheap = (per_lesson["Gemini 3.1 Flash-Lite (used today)"] * CONCEPTS * FX + extras_2y) * n / 1e5
    cheap3 = (per_lesson["Gemini 3.1 Flash-Lite (used today)"] * CONCEPTS * FORMATS * FX + extras_2y) * n / 1e5
    pro = (per_lesson["Gemini 2.5 Pro"] * CONCEPTS * FX + extras_2y) * n / 1e5
    pro3 = (per_lesson["Gemini 2.5 Pro"] * CONCEPTS * FORMATS * FX + extras_2y) * n / 1e5
    calls = n * CONCEPTS * 3 * ROUNDS
    print(f"  {n:>9,} students: ours {ours:9.1f} | flash-lite explain {cheap:9.1f} | flash-lite 3 fmt {cheap3:9.1f} | pro explain {pro:9.1f} | pro 3 fmt {pro3:10.1f} | per-student model calls {calls/1e6:,.1f}M")

price_year = 100 * 12
print(f"\nas % of an assumed Rs {price_year}/year price (Rs 100/month), per student per year:")
print(f"  ours AI {EXTRAS_MONTH_INR*12/price_year:.1%}")
for m, usd in per_lesson.items():
    y = usd * CONCEPTS * FX / 2
    print(f"  per-student {m}: explain {y/price_year:.1%}, 3 formats {3*y/price_year:.1%}")
print(f"\nstorage per student: {CONCEPTS*6434/1e6:.1f} MB explain, {CONCEPTS*FORMATS*6100/1e6:.1f} MB 3 formats")
