# EcoLearn: HackAStone 2026 finals, speaker transcript

Deck: `EcoLearn_Hackastone.pptx` (31 slides). Talk: **15 minutes, two presenters, screen-shared from laptops.**
About 2,200 spoken words (A ~1,080, B ~1,110), at ~145 words a minute. The clock at each slide is the target
*start* time; if you are more than 30 seconds behind, use the cut list at the end.

| | Slides | Part | Time |
|---|---|---|---|
| **Presenter A** | 1–12 | The problem, our solution, how it works, the agents, meet Aarav, his first three steps | 0:00–7:30 |
| **Presenter B** | 13–31 | The learning loop, the teacher, what it measures, readiness, business, close | 7:30–15:00 |

**One handoff, at slide 13.** If you switch screen share between laptops, B should have the deck open
in presenter mode **on slide 13** before A reaches slide 11, and A stops sharing only after saying the
handoff line. (Simplest and safest: A keeps sharing and clicks while B talks; then no switch is needed.)

**The message to repeat, in your own words, at slides 1, 4, 29 and 31:** EcoLearn is not a physics
app. The engine is subject-independent; physics is the example we built for the demo. A new subject is
new content (concepts, lessons, the known mix-ups), not new software.

**Stay honest on stage:** Aarav and his class are a sample class we built. The numbers on slides 25–28
are a *simulated* class computed by the real product. The story on slide 13, the tutor's answer on 16
and the lesson plan on 20 are real AI outputs.

---

## PRESENTER A

### Slide 1 · Title (0:00)
Good morning. We are team EcoLearn, under the guidance of Professor M C Chinnaiah. I'm *[name]*, and
with me is *[name]*.

EcoLearn is an AI tutor that teaches every concept through something the student already loves. For
this competition we built it for Class 11 and 12 physics. But one thing to keep in mind for the next
fifteen minutes: **nothing in EcoLearn is physics-specific.** Physics is our example. The same software
can teach chemistry, maths or biology, because a new subject is new content, not new code.

These five pictures are from our real lessons on Newton's laws: the same law, through cricket,
football, gaming, smartphones and motorsport.

### Slide 2 · Learning today (0:45)
Learning has changed. More and more of it happens alone: homework, revision, videos, apps, at the
student's own pace. That's good. It builds independence and it works anytime, anywhere.

But learning on your own is fragile, and four things go wrong. **Motivation fades**: nobody is nearby
to keep you going when it gets hard. **The content is one-size-fits-all**: the same explanation for
everyone. **Mistakes go unseen**: nobody spots the wrong idea behind a wrong answer. And **feedback
comes late**, often at the exam, when it's too late to fix.

### Slide 3 · Problem statement (1:35)
So our problem statement is this. *(Read it slowly.)*
"Generic learning ignores individual interests and ways of understanding, leading to disengagement
and reduced motivation."

The chain is simple: generic content, so no link to how I think, so motivation drops. And when a
student learns alone, nobody is there to break that chain.

### Slide 4 · Our solution (2:10)
Our answer is EcoLearn, which fits the content to the learner instead of the other way round. It does
four things.

It **gets to know the learner**: their interests, their hobbies, how they like to learn, and a
five-minute starting check. It **teaches through their world**: every concept through cricket,
football, gaming, phones or motorsport, plus a short story about their own hobby. It **finds the exact
mix-up**: every wrong answer points to the specific idea to fix, and the path adapts. And it **keeps
them going**: practice, revision at the right moment, and progress they can see.

And the teacher stays in the loop: they see where the class is stuck, and AI helps them plan what to do
next.

What you'll see today is Class 11 and 12 physics for the Indian boards, CBSE and ISC. That's the demo,
not the limit: the same four steps work for any subject.

### Slide 5 · How EcoLearn works (3:10)
There are two loops.

The top loop happens **once, in advance.** We start from the curriculum: the concepts, their teaching
order, and the known mix-ups for each. For the demo that's the physics syllabus; for another subject,
it's that subject's syllabus. A lesson is written for each concept in each interest, following a written
guide, and every lesson is checked before any student sees it. The library then serves it instantly.

The bottom loop is **live, for one student.** We take their own lesson and their profile: their
hobbies and the mix-ups from their starting check. An AI writer drafts a story around their hobby,
grounded only in that lesson. Rules and a second AI check the physics, the analogy and its safety; a
failed draft is rewritten. If anything fails, the student simply gets the prepared story. Then their
answer to the check updates their plan, their mix-ups and their revision.

### Slide 6 · Our agent system (4:10)
This is the agent system, and we are clear about which parts are AI.

On the left, three AI agents for the student: a **story writer with a critic** that checks it, a
**doubt chat** that answers from the student's own lesson, and **practice questions** written by one
AI and solved independently by another before a student sees them.

On the right, everything that *judges* a student: the profile, the learning path, the graded checks and
mastery. **These are rules, on purpose**, so the same answers always get the same result. No AI marks
anyone.

At the bottom, two AI agents for the teacher: a **teaching assistant** that plans the next lesson, and
a **coaching agent** that suggests one action per student, which the teacher approves. Every AI agent
has a safe, non-AI fallback.

### Slide 7 · A case study (5:00)
Instead of going feature by feature, let's follow one student, Aarav, from his first sign-in to his
teacher's next lesson. Everything you'll see is the real, working product. Aarav and his classmates
are a sample class we built for demos, so none of these numbers are pilot results.

### Slide 8 · Meet the student (5:20)
This is Aarav, Class 11. He wants to crack an entrance exam, but he says he *dreads* physics, his maths
is shaky and numericals trip him up. He learns best by trying an example first, in short ten-minute
sessions. He loves cricket, watches badminton and follows kabaddi.

These are his own answers to EcoLearn's first-sign-in questions. A textbook gives him the same page as
everyone else. Let's see what EcoLearn does with them.

### Slide 9 · The journey at a glance (5:50)
Here is the whole journey. Three steps to get started: tell us about you, a starting check, and a path
made for him. Then a loop that repeats for every concept: a lesson in his world, a quick check, a wrong
answer turned into what to fix, help from an AI tutor, revision, and a page where he sees what EcoLearn
thinks of him. And alongside it, his teacher.

### Slide 10 · Step 1, sign in (6:15)
His teacher created his account: a username and password, **no email, no phone number**, because
these are minors and we collect as little as we can. The first time he signs in, EcoLearn asks about
*him*, not about physics: his hobbies, how he likes to learn, how long he can focus, how he feels about
the subject. About four minutes of taps, and any question can be skipped. No AI here: plain rules use
these answers to shape his lessons.

### Slide 11 · Step 2, starting check (6:45)
Then a five-minute starting check: eight multiple-choice questions, no marks, and "I'm not sure yet"
is allowed. The key design choice: **every wrong option was written to catch one specific
misconception.** So a wrong answer doesn't just say "wrong", it says *which idea* he has mixed up. It's
graded by rules, so the result is the same for every student.

### Slide 12 · Step 3, his path (7:10)
That check becomes his own map. What he already knows is marked done, and the two ideas he mixed up go
to the top. Chapters are always open; inside a chapter, concepts unlock in order. And "Revise now"
brings ideas back before he forgets them.

**Handoff:** Now *[B's name]* will take you through what happens when Aarav actually starts learning.

---

## PRESENTER B

### Slide 13 · Step 4, the lesson (7:30)
Thank you. Step four, the lesson. The lesson itself is a prepared, checked cricket lesson. Because
Aarav likes to start by trying, "try an example" comes first for him.

On top of it, an AI agent writes a short personal story around his own hobby, badminton: here, using
the net as the zero point for position. A second AI acts as a critic and must pass it before he ever
sees it. This is a real story the AI wrote. And if the AI is slow or fails, he gets the prepared story,
so nothing breaks.

### Slide 14 · Step 5, quick check (8:05)
After the lesson, one question, again in cricket: a fielder runs 25 metres in and 10 back; what
distance did she cover? Before he answers, Aarav says how sure he is. That matters: **sure but wrong**
is a firmly held misconception, the kind worth a teacher's minute.

The line "Before you pick, read each option once more" is our pilot experiment: a random half of each
class sees it, the other half doesn't, and we compare first-try accuracy.

### Slide 15 · Step 6, a wrong answer (8:35)
Aarav picks 15 metres, and he was sure. Instead of just "wrong", EcoLearn says "not quite, and that's
useful", and names the exact slip: he subtracted the way back, which gives displacement, not distance.
The mix-up goes on his list and the idea comes back sooner for revision.

If he wants more, he can ask for a practice question: one AI writes it, a second AI solves it without
seeing the answer, and he only sees it if they agree. Practice never counts towards his marks.

### Slide 16 · Step 7, stuck? Ask (9:05)
Still unsure, he asks in his own words: "why can displacement be zero when I ran a lot?" This is a real
answer from the AI, grounded in his own lesson and in cricket: run to the other crease and back, and
your displacement is zero.

Before any AI sees a question, a safety layer stops personal details, unsafe topics and attempts to
trick the model. We log only the outcome, never the words.

### Slide 17 · Step 8, mix-ups and revision (9:30)
"My mix-ups" lists every misconception he has shown, and the ones he has fixed. And an idea only counts
as **mastered** when he gets two *different* questions right, so a lucky guess doesn't count. Mastered
ideas still come back after 7, 21 and 63 days.

### Slide 18 · Step 9, about me (9:50)
Many apps profile students silently. EcoLearn **shows** Aarav what it thinks of him, with the evidence:
"4 of 11 answers you were sure about were wrong", and what it changes because of that. If it's not
him, one tap on "That's not me" switches it off.

### Slide 19 · For the teacher (10:15)
Now the teacher, because this is where EcoLearn is most different: a teaching assistant, not another
dashboard. A class is set up in two minutes: paste names, print login slips. Two of these tools are AI:
a lesson plan for tomorrow and a coaching note per student. The AI never sees a name, and the teacher
always decides.

### Slide 20 · His teacher, the same evening (10:45)
Aarav's teacher opens the class page. First, who needs attention, found by rules. Below it, the AI teaching assistant reads what the class actually did
and writes a ten-minute starter for tomorrow. Students reach the AI only as S1, S2, and names are put
back for the teacher afterwards. This is a real plan, and Aarav is one of three students it says to
check in with.

### Slide 21 · The whole class at a glance (11:10)
One row per student: interest, concepts mastered, reading time, right first time, last active. The
teacher can move students between classes, reset passwords, and switch AI off for any student whose
family says no.

### Slide 22 · The mix-up map (11:25)
Because every wrong option maps to a misconception, this page reads like a **diagnosis, not a mark
sheet.** At the top: Newton's first law, where the students who missed it forgot the normal force. A
teacher can plan tomorrow's first ten minutes from this one card.

### Slide 23 · Coaching notes (11:45)
For each student, an AI reads a small case file, never the name, and suggests one thing to try, with
the evidence. And the suggestion is a button: "Add Newton's third law to their revision list". The
teacher approves, EcoLearn carries it out, and reports back whether the student did it.

### Slide 24 · How the AI decided (12:05)
Schools are rightly nervous about AI writing for children. So the teacher sees every AI story: drafted,
rejected, rewritten or fallen back, with a decision log, and can hide any of them. That's responsible AI: not a
promise, but a page the teacher can check.

### Slide 25 · What EcoLearn measures (12:25)
What does a school get? Here is a full class of 25 over three weeks. **Please read this as what
EcoLearn measures, not as results: the class is simulated.** We generated the answers with a script,
but every number is computed by the real product. 23 of 25 students active, and the teacher is told
about the two who never started; 204 lessons opened; 79 percent right first time; 78 percent said the
lesson helped.

### Slide 26 · A built-in comparison (12:55)
EcoLearn also builds in a rough control: ideas a student studied versus ideas they didn't. Studied
ideas went from 18 to 73 percent. But we are careful: students study exactly what they got wrong, so
some rise is expected anyway. That's why our real pilot is randomised and written down before it
starts.

### Slide 27 · Which concepts moved (13:15)
For the teacher, per idea: acceleration moved most, 57 to 86 percent; Newton's first law had the most
mix-ups fixed; projectile motion is still weakest, so that's tomorrow's lesson.

### Slide 28 · What a score alone hides (13:30)
And a score says "wrong". EcoLearn says *which idea, who, and how sure they were*: here, every student
who missed the wet-covers question thought the ball curves down because its weight is unbalanced. They
forgot the normal force.

### Slide 29 · Technology readiness (13:45)
Is it real? It runs in any browser, phone or laptop. Every AI part has a fallback, so it keeps working
when the AI is down, and changing the AI provider is a setting, not a rebuild. Everything on the right
works today, with automated tests across the system. And again: physics is just what we loaded first;
nothing on this slide changes for another subject. Our next step is a school pilot.

### Slide 30 · Commercial viability (14:15)
Is it a business? Lessons are made once and shared by every student, so AI adds only a few rupees per
student per month. Schools pay per student, or students use it free and schools pay for the teacher
dashboard; we still have to validate pricing with schools. And it grows cheaply: **a new subject, board
or language is new content, not new software.**

What sets us apart is on the right: their world, personal but correct, the exact mix-up, the teacher in
the loop, safe for minors, and never leaving a student stuck.

### Slide 31 · Thank you (14:50)
Thank you. EcoLearn: learning that speaks each learner's language. Today in physics, tomorrow in any
subject. We'd love your questions.

---

## If you are running late (cut in this order)

1. **Slide 21**: one sentence ("one row per student, and the teacher can switch AI off for any family that says no").
2. **Slides 26 and 27**: click through with one line each, or skip 27.
3. **Slide 9**: "Nine steps, one loop; let's walk through it."
4. **Slide 17**: just "mastered means two different questions right."

Never cut: slide 3 (the problem statement), the "simulated" sentence on slide 25, and the "any subject" line on 30.

## Likely questions (who answers)

- **"Why only physics?" (A)** It's our example, chosen because it's abstract and students fear it. The engine has
  no physics in it: a subject is a curriculum file (concepts, order, mix-ups) plus lessons. Adding chemistry or maths
  is writing content, not changing code.
- **"Who writes the lessons? Can the AI get physics wrong?" (A)** Lessons are prepared in advance with a written guide
  and an automated checker, never generated live for a student. Only the short personal story is live, and a second
  AI plus rules check it; if anything fails the student gets the prepared story. A subject teacher reading every
  lesson is part of the pilot plan.
- **"Is there evidence it works?" (B)** Not yet, and we say so: today's numbers are a simulated class. The pilot is a
  randomised comparison, decided before it starts.
- **"Children's data?" (B)** No email or phone, the AI never sees a name, the AI can be switched off per student, and a
  student's data can be exported or erased.
- **"What does it cost?" (B)** Lessons are shared, so the per-student cost is the small AI layer: a few rupees a month.
- **"Why not let the AI grade?" (A)** So the same answers always get the same result, and so pilot numbers come from
  fixed, validated questions. AI helps; rules judge.

> Note: slide 31 (and the tagline under the title) say "Physics that speaks each learner's language". If you want
> the slide to match the "any subject" message, change it to "Learning that speaks each learner's language".
