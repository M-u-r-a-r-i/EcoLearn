# EcoLearn pilot: consent note (DRAFT)

Draft of 2026-10-13. **Not legal advice and not ready to send.** Part A is for the school and a lawyer. Parts B to D are the
note for families, once the square brackets `[like this]` are filled in and the open decisions in Part A are made.

---

## Part A. For the school and your lawyer (do not send to families)

### What this is

A draft consent note for a pilot of EcoLearn, a physics tutor for Class 11 and 12 (CBSE and ISC), with students who are
under 18. Every factual statement in Parts B to D was checked against the product on 2026-10-13 (table at the end of
this part). Where the product cannot yet do something the note would naturally promise, this part says so.

### Fill in before use

| Blank | What goes there |
|---|---|
| `[School]` | The school running the pilot |
| `[Operator]` | Who runs EcoLearn (name, address) |
| `[Contact]` | A named person, email and phone for questions and requests |
| `[Grievance contact]` | The person who handles complaints about personal data |
| `[Retention]` | How long data is kept after the pilot ends (see decision 3) |
| `[Hosting]` | Where the server is and who runs it (see decision 4) |
| `[Provider terms]` | Which AI service and plan is used, and what its terms say (see decision 4) |
| `[Safeguarding]` | Option 1 or Option 2 from decision 2 |

### Decisions the school has to make

1. **Who is responsible for the data.** Is the school the party that decides how the data is used, with EcoLearn working for
   it, or is EcoLearn's operator? The answer changes who signs, who answers complaints and which exemptions may apply.
   Ask the lawyer.
2. **What happens after a student writes about harming themselves.** The help chat answers with a supportive message,
   suggests a trusted adult, and gives the free Tele-MANAS helpline (14416) and 112. Nobody is told: the question is not
   stored and a keyword match can be wrong. Choose one, and put it in Part B:
   - **Option 1 (nobody is told).** "The chat does not alert anyone."
   - **Option 2 (a person is told).** The school's counsellor is alerted, for example by a daily count or by name. **This is not built.** It needs
     work on the software and a clear policy on who acts, how fast, and what is recorded. Do not choose it until that exists.
3. **How long to keep the data.** Suggested: delete personal data `[3] months` after the pilot ends, keep only de-identified
   totals. The operator erases a student with `scripts/delete_student.py` (built 2026-10-13, see "Built, with limits"). It
   cannot reach **backups or earlier copies of the database**, so the retention rule must say how long those are kept.
4. **Hosting and the AI service.** Where the server runs, and whether the AI service is on a paid plan. Google states its
   free tier may use data to improve its products and its paid tier does not (pricing page, checked 2026-10-13). Use a
   paid plan for children's data, confirm in writing where data is processed, and fill in `[Provider terms]`.
5. **Whether a family can say no to the AI parts and still take part.** They can since 2026-10-14 (see "Built, with
   limits"). Decide how a family says so: the optional box on the form in Part D, or a request to `[Contact]`.

### Built, with limits (2026-10-13)

- **Erasing a student:** `scripts/delete_student.py --username X --export DIR --confirm`. It is a dry run unless `--confirm` is
  given. It removes the account and every row tied to it in one all-or-nothing step, then searches the whole database to prove
  nothing is left. The AI usage log keeps its token counts but loses the link to the child; the student's label and note in class
  plans are removed. **Not touched: backups and any earlier copy of the database.**
- **Showing a family what is held:** `scripts/export_student.py --username X --out DIR`: a plain-language summary and the full
  data as JSON. The password is never included.
- **Switching the AI off for one student** (2026-10-14): the teacher's Students tab ("AI off"), or
  `scripts/set_student_ai.py --username X --off` by the operator. With it off, nothing about the student is sent to an AI service: no
  personal story is written or shown, the help chat answers with the lesson's own key idea, their teacher note is written by fixed rules,
  and the class plan leaves them out. Lessons, quizzes and progress work the same (none use AI). Tested by `tests/test_ai_switch.py`.
  It does not reach back: a story or note written before the switch stays stored until the student is erased.
- **Export and erase are run by a person on the operator's team**, not by a family or a teacher through the app. Who runs them, how identity is
  checked, and how fast is for the operator and school to decide (the note has a `[number]` of days). Tested by
  `tests/test_student_data_rights.py`: every table that holds a student id is covered, and the test fails if a new one is added.

### Things the product cannot yet do (build them, or remove the promise)

| The note would like to promise | The software today | Needed |
|---|---|---|
| "A counsellor will be told" | Not built (decision 2). | Software and a policy |
| "Only [Operator]'s named staff can read your child's data" | Anyone with the database file can. The pilot report replaces names with codes, but the database itself is not encrypted. | Access rules for the server, and ideally an encrypted disk |

The note in Part B is written so that it is **true today**: it offers a copy and deletion on request and switching off the AI
parts (built), and does not promise a counsellor alert. Update it when that exists.

### Legal points to check with a lawyer

I'm not a lawyer. This is what a search on 2026-10-13 found; the sources disagree on dates and rule numbers, so read the
gazetted text.

- India's Digital Personal Data Protection Act, 2023 treats anyone under 18 as a child (section 2(f)). Section 9 asks for
  **verifiable consent from a parent or guardian** before processing a child's data, bars processing likely to harm a
  child's well-being, and bars **tracking or behavioural monitoring** of children.
- The DPDP Rules 2025 give educational institutions a **narrow** exemption from the consent and tracking provisions, limited
  to processing for the institution's own educational activities or for children's safety. Commentary says it is unclear
  whether an edtech platform counts as an educational institution.
- EcoLearn does record behaviour (reading time, how often lessons are skimmed, what a student gets wrong, a "needs
  attention" list for the teacher). That is educational and is shown to the teacher, but a lawyer should say whether it falls
  under the exemption or needs parental consent. **This draft assumes it needs consent** and asks for it.
- The CBSE and ISC boards, and any state or school policy on apps and student data, may add rules.
- Sources: [DPDP section 9 summary](https://dpdp.myndsolution.com/wiki/act/section-9-processing-of-personal-data-of-children/index.md),
  [Tsaaro: regulatory carve-outs](https://tsaaro.com/blogs/regulatory-carve-outs-examining-exemptions-under-the-dpdp-act-2023-and-dpdp-rules-2025),
  [CyberPeace on tracking and monitoring](https://cyberpeace.org/resources/blogs/prohibition-of-behavioral-tracking-and-targeted-advertising-for-children-under-the-dpdp-act-2023).

### Where each statement comes from

| The note says | Evidence in the product |
|---|---|
| No email, phone, photo, voice or location is collected | Accounts are a name, username and password (`src/auth/`, `tests/test_auth.py`); nothing else is asked |
| Passwords are stored scrambled | bcrypt hashes (`src/auth/passwords.py`) |
| Survey answers are picked from fixed options and all optional | `data/survey.yaml`, `tests/test_survey.py` |
| A teacher sees a summary of the survey, not the raw answers | `tests/test_survey.py` |
| EcoLearn never sends a name from its records to the AI (a child could still type one into the help chat; the note says so) | `tests/test_personal_story.py`, `tests/test_teacher_agent.py`, `tests/test_coaching_agent.py` |
| The only typed text that reaches the AI is a short hobby label and a help-chat question | the same tests; `src/learner/help_guard.py` |
| Help-chat questions are checked, rate-limited and never stored | `src/learner/help_guard.py`, `tests/test_help_guard.py` |
| A student can report a story, a teacher can hide it | `tests/test_story_review.py` |
| The AI parts can be switched off for one child, and then nothing about them is sent to an AI service | `scripts/set_student_ai.py`, the teacher's Students tab, `tests/test_ai_switch.py` |
| A family can be shown, and can have deleted, everything held about their child | `scripts/export_student.py`, `scripts/delete_student.py`, `tests/test_student_data_rights.py` (backups are not covered) |
| AI is not used for marks | Grading is multiple choice against an answer key (`tests/test_mcq_grading.py`) |
| The lessons were prepared in advance with AI help and checked by software | `PROJECT_HISTORY.md`; `scripts/validate_lessons.py`. A person has not read every lesson |
| Pilot results are reported without names | `scripts/pilot_report.py` (pseudonyms S001...), `tests/test_pilot_survey.py` |

The fuller picture of the AI, with test results and known gaps, is the AI safety card (`docs/ai-safety-card.html`). Give
the school that too.

---

## Part B. Note for parents and guardians

**EcoLearn pilot at [School]: what it is and what we keep**

Dear parent or guardian,

[School] is trying out **EcoLearn**, a physics tutor for Class 11 and 12, from [Operator], for [number] weeks starting
[date]. Your child's teacher sets up their account. We are asking for your permission for your child to take part,
because they are under 18. Please read this note and tell us if you have questions.

**What EcoLearn does.** Your child answers a short "starting check", then works through physics lessons in a topic they like
(for example cricket or football). Quick quiz questions show what they have understood and which ideas they mix up. Their
teacher sees how the class is doing and plans lessons around it. At the end there is a second check, so we can see what
changed.

**What we keep about your child**

| What | Why |
|---|---|
| Name, a username, and a password (stored scrambled, so nobody can read it) | So they can sign in |
| Class (11 or 12) and class group | To show the right chapters and let the teacher see the class |
| The topic they chose for lessons, and hobbies (picked from a list, plus up to two they type, at most 24 letters) | To build lesson examples around what they like |
| Answers to a short "getting to know you" survey: how they like to learn, how long they focus, how they feel about physics and maths, their goal. Picked from fixed options; every question can be skipped. If your child updates their answers later, the earlier answers are kept as history for the pilot's evaluation, and the teacher does not see that history | To shape lessons, and to give the teacher a summary |
| Which lessons they opened, how long they actively read, and thumbs up or down | To see progress and what is confusing |
| Their answers to quiz questions and the starting and end checks, and how sure they said they were | To track progress and find ideas they mix up |
| Short pieces of text written by the AI for them (see below) | So they can be shown and checked |
| Short notes for the teacher, written by the AI or by fixed rules, about how each student is getting on | To help the teacher support each student |
| What happened to each question they asked in the help chat (answered, stopped, or too many), but **not** the words | To keep the chat safe |
| When they last used EcoLearn | To help the teacher see who needs a nudge |

**What we do not collect:** an email address, a phone number, a home address, photos, voice, location, or contacts.
Ordinary technical logs are kept by the server `[Hosting: say what, and for how long]`. Small settings, such as light or dark
theme, are kept in your child's own browser.

**Who can see it**
- **Your child** sees their own progress.
- **Their teacher** sees the class: progress, quiz answers, the survey summary (not the raw answers), the AI-written
  text, and the notes. This is the point of the tool.
- **[Operator]'s named staff** `[names or roles]` see it to run and support the pilot.
- **Results of the pilot** may be reported, for example in a school report or a presentation. These use totals and averages
  with names replaced by codes. They never name a child.
- **Not sold, not shared** with advertisers or anyone else, and not used to show your child adverts.

**How AI is used.** EcoLearn uses AI in four places, and every one has a plain version that works without it:
1. a short **personal story** about a hobby, at the top of a lesson;
2. a **help chat**, where your child can type a question about a lesson;
3. a **class plan** for the teacher; and
4. the **short notes** for the teacher.

**You can say no to the AI parts** and your child can still take part: tick the box on the form or tell `[Contact]`, and
their teacher switches them off. Then nothing about your child is sent to an AI service; they get the lesson's own story, and the help
chat shows the lesson's key idea instead of an AI answer. Lessons, quizzes and progress work the same.

The lessons and quiz questions were prepared in advance, with the help of AI, and checked by software `[and read by
(who)]`. **AI does not mark or grade anything.** Quiz answers are checked against an answer key.

EcoLearn never sends your child's name to the AI. For the help chat, the **question your child types** is sent to the AI service
`[Provider terms]` to be answered. We tell children not to share personal details (including their own name), and the chat will not send
questions that contain things like phone numbers or email addresses. The AI can be wrong. Stories are checked by a second AI and by rules,
a student can report a story, and a teacher can hide it. The lesson itself is always there.

**If your child is upset.** If a student types something that suggests they may harm themselves, the chat replies kindly,
suggests talking to a trusted adult, and gives the free helpline Tele-MANAS (14416) and the emergency number 112.
`[Safeguarding: choose Option 1 or Option 2 from Part A]`

**Your choices and rights**
- **Taking part is voluntary.** If you say no, or later change your mind, there is no effect on your child's marks or place
  at school.
- You can **ask to see** what we hold about your child (we will give you a copy in plain words), **ask us to correct it**, or
  **ask us to delete it**, or withdraw your consent, at any time, by contacting `[Contact]`. We act within `[number]` days.
  Deleting is permanent. Copies in backups are removed when the backups `[are deleted or expire after (number) days]`.
- You can complain to `[Grievance contact]`.

**How long we keep it.** Until `[Retention]`, or sooner if you ask. After that we keep only totals with no names.

**How we protect it.** Passwords are stored scrambled. Accounts need a sign-in. The service is hosted `[Hosting]`.

**Questions?** `[Contact]`.

---

## Part C. For students (15 to 17), to read with the family

**Using EcoLearn: what you should know**

- EcoLearn is a physics tutor. Your teacher made your account. You don't need an email.
- It remembers your name, class, what you answer, how long you read, and what you say in the "getting to know you" questions.
  You can skip any of those questions. Your teacher sees a **summary** of the survey, not your exact answers.
- Some bits are written by **AI**: a short story about one of your hobbies, answers in the help chat, and notes for your
  teacher. AI can get things wrong. If a story seems wrong or odd, press "Something wrong with this story?". AI never gives
  you a mark.
- In the help chat, **don't type your phone number, email, address, or anything private.** The chat will refuse those.
  Your question is sent to an AI service so it can answer. EcoLearn doesn't send your name.
- If you are ever upset or worried, talk to an adult you trust: a parent, a teacher or the school counsellor. You can call
  **14416** (Tele-MANAS, free, any time). In danger right now, call **112**.
- Your family can ask for the AI parts to be switched off for you. Everything else works the same.
- You can say no, or stop, any time. It won't affect your marks.

---

## Part D. Consent form

**EcoLearn pilot at [School]**

Parent or guardian:

- [ ] I have read the note above and had the chance to ask questions.
- [ ] I agree that my child may take part in the EcoLearn pilot, and that the information described in the note may be kept
      and used as described, including sending the questions my child types in the help chat to the AI service named in the
      note.
- [ ] **Optional:** I would like the AI parts switched off for my child (no AI story, no AI help chat, not included in the
      AI's notes or class plans). My child can still use the lessons and quizzes.
- [ ] I understand I can change my mind at any time by contacting `[Contact]`, and that this will not affect my child's
      place or marks at school.

| | |
|---|---|
| Child's name | |
| Class and section | |
| Parent or guardian's name | |
| Relationship to the child | |
| Signature | |
| Date | |

Student (assent): I have read the student page and I am happy to take part.  Name: ____________  Signature: ____________  Date: ________

*Return to `[Contact]` by `[date]`. A translation into `[language]` is available on request.* `[Have the note translated before it goes out.]`
