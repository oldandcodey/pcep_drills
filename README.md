# PCEP / Python Essentials 1 — Two-Week Drill Program

**Target exam:** PCEP-30-02 (Certified Entry-Level Python Programmer)  
**Aligned course:** Python Essentials 1 (Edube / Cisco NetAcad, free)  
**Cadence:** ~15 minutes per weekday. Weekend = wrap, test, document, commit.  
**Deliverables:** two small CLI programs in one Git repository.

Official syllabus blocks (memorize the weights; the exam does):

| Block | Name | Weight | Items |
| --- | --- | --- | --- |
| 1 | Computer Programming and Python Fundamentals | 18% | 7 |
| 2 | Control Flow — Conditional Blocks and Loops | 29% | 8 |
| 3 | Data Collections — Tuples, Dictionaries, Lists, and Strings | 25% | 7 |
| 4 | Functions and Exceptions | 28% | 8 |

Passing score: 70%. Question style is not only multiple choice: gap-fill, code insertion, drag-and-drop sequencing. You must *type* correct syntax, not merely recognize it.

Free prep: [Python Essentials 1 on Edube](https://edube.org/study/pe1) or NetAcad. Use this program as the *practice* layer, not a substitute for the course modules.

---

## How each 15-minute session works

1. **5 minutes — Exam drill.** Read the day's objective list. Write one tiny snippet from memory (no peeking). Say the terms out loud: interpreter vs compiler, binding, shadowing, `None`, exception hierarchy.
2. **10 minutes — Build.** Implement only that day's slice of the project. Stop when the timer ends. A half-finished function is a valid commit.
3. **Git (2 extra minutes, non-negotiable).** Stage, commit with a verb-first message (`Add input loop for checklist items`). Never commit broken syntax if you can avoid it; do commit incomplete features.

Repository layout from day one:

```
pcep-drills/
├── README.md
├── .gitignore
├── week1_resilience/
│   └── resilience_check.py
└── week2_brief/
    ├── brief_builder.py
    └── brief_lib.py
```

`.gitignore` at minimum:

```
__pycache__/
*.pyc
.venv/
.env
*.json
```

Create the repo on day 1. Use a `main` branch. Each week gets a `week1` / `week2` branch merged back when the program runs end-to-end.

---

## Week 1 — Program: Home Resilience Checklist (`resilience_check.py`)

**Why this program.** You already think in generator, solar, hurricane kit, and household readiness. The program is a console checklist: add items, mark status, print a readiness report. It is not clever. It is exam-shaped.

**PCEP coverage:** Blocks 1–3 almost entirely. Block 4 only at the edges (you will *use* built-ins; you will not yet *define* many functions).

### Day 1 — Fundamentals, literals, variables, I/O
**Exam objectives:** 1.1–1.3, 1.5  
Interpreter vs compiler. Keywords, indentation, comments. `int` / `float` / `str` / `bool`. Naming / PEP 8. `print()`, `input()`, `sep=`, `end=`, `int()`, `float()`.

**Build:** Banner, ask for operator name and date, print a formatted header.

```python
# resilience_check.py — Day 1
print("NAVARRE RESILIENCE CHECK", sep=" ", end="\n")
name = input("Operator name: ")
print("Logged in as", name, sep=": ")
```

**Drill:** Convert `"12"` and `"3.14"` with `int()` / `float()`. Print `0b1010`, `0o12`, `0xA`. Explain why `0.1 + 0.2 != 0.3`.

### Day 2 — Operators, types, booleans
**Exam objectives:** 1.4  
Arithmetic (`** * / % // + -`), string `+` `*`, shortcuts, unary/binary, precedence, bitwise (`~ & ^ | << >>`), `and`/`or`/`not`, relational, casting.

**Build:** Ask how many gallons of generator fuel on hand and the minimum required. Compute shortfall. Boolean: `ready = on_hand >= minimum`.

**Drill:** Predict results without running:

```python
print(2 ** 3 ** 2)      # right-associative
print(5 / 2, 5 // 2, 5 % 2)
print(True + True)      # bool subclass of int
print(not 0 and 3)
```

### Day 3 — `if` / `elif` / `else`, nesting
**Exam objectives:** 2.1  
All four forms. Multiple conditions. Nested `if`.

**Build:** Readiness bands.

- fuel >= min **and** kit complete → `GREEN`
- fuel >= min **or** kit complete → `AMBER`
- else → `RED`

Nest one extra check: if `RED` and hurricane season month, print an extra warning.

**Drill:** Write an `if-elif-else` that maps a 0–100 score to letter grades. Nest a second `if` inside `A` for "high A".

### Day 4 — `while`, `for`, `range`, `break` / `continue` / `pass`
**Exam objectives:** 2.2  
`while`, `for`, `range()`, `in`, `while-else` / `for-else`, nesting, `break`, `continue`, `pass`.

**Build:** Menu loop.

```
1 Add item
2 List items
3 Quit
```

`while True` + `break` on quit. `continue` on invalid choice. `pass` as a placeholder for a future "save" option.

**Drill:** Print even numbers 0–20 with `range`. Use `continue` to skip 10. Use `for-else` to detect "10 never appeared" (it will not fire if you `break`).

### Day 5 — Lists
**Exam objectives:** 3.1  
Construct, index, slice, `len()`, `append()`, `insert()`, `index()`, `del`, `in` / `not in`, `sorted()`, iteration, copy vs clone, list-of-lists.

**Build:** `items = []` of strings. Add / list / remove by index. Slice last three added. Demonstrate `b = a` vs `b = a[:]` by mutating one and printing both.

**Drill:** Build a 3×3 matrix as lists-in-lists. Print the diagonal. That question appears on exams.

### Day 6 — Tuples and dictionaries
**Exam objectives:** 3.2, 3.3  
Tuple immutability, packing/unpacking, list-inside-tuple. Dict build, key add/remove, `keys()` / `values()` / `items()`, membership of keys.

**Build:** Each checklist row becomes a dict: `{"name": "5-gal fuel can", "qty": 2, "ok": False}`. Store them in a list. Categories as a tuple `("POWER", "WATER", "COMMS", "MED")` — immutable on purpose.

Print a report by iterating `.items()`.

**Drill:** Why `t[0] = 1` raises `TypeError`. Why `d[[1,2]] = 3` raises `TypeError`. What `d.get("missing")` returns vs `d["missing"]`.

### Day 7 — Strings + Week 1 wrap
**Exam objectives:** 3.4  
Construct, index, slice, immutability, escapes, quotes inside quotes, multi-line, basic methods (`upper`, `lower`, `strip`, `split`, `join`, `find`, `replace`, `startswith`).

**Build:** Render a multi-line readiness report with f-strings or `.format()`. Title-case item names. Join categories with ` | `.

**Weekend wrap (30–45 min, once):**

- Run the whole script. Break it on purpose (bad index, empty list) and watch the traceback — you will handle those next week.
- Write a 20-line README: purpose, how to run, sample session.
- Commit on `week1`. Merge to `main`. Tag `v0.1-week1`.
- Self-test: can you explain every line without notes? If not, that line is tomorrow's drill.

**Week 1 definition of done:** one `.py` file, no functions required yet, menu works, list + dict + tuple all appear, report prints, Git history is readable.

---

## Week 2 — Program: Daily Brief Builder (`brief_builder.py` + `brief_lib.py`)

**Why this program.** You already draft client/AI/cyber notes and personal logs. This tool takes a few fields and emits a short structured brief. Week 2 exists to force **functions and exceptions** — the 28% block people under-practice because it feels "already known."

**PCEP coverage:** Block 4 in full. Rehearse Blocks 1–3 by refactoring Week 1 patterns into functions.

### Day 8 — Define / call / `return` / `None`
**Exam objectives:** 4.1 (first half)  
`def`, invoke, `return`, implicit `None`, generators mentioned (know `yield` exists; you need not master it).

**Build:** `brief_lib.py`

```python
def banner(title):
    return title.upper()

def empty_brief():
    return None
```

Call them from `brief_builder.py`. Print `type(empty_brief())`.

**Drill:** What does a function return if it has no `return`? What if it has `return` with no value? Write a one-line generator (`yield`) so the word is not foreign on exam day.

### Day 9 — Parameters, arguments, defaults, scope
**Exam objectives:** 4.2  
Positional vs keyword vs mixed. Defaults. Local vs global. Shadowing. `global`.

**Build:**

```python
def format_item(name, qty=1, ok=False):
    status = "OK" if ok else "OPEN"
    return f"{name} x{qty} [{status}]"
```

Call three ways: positional, keyword, mixed. Add a module-level `OPERATOR` and a function that *shadows* it, then one that uses `global`. You will dislike `global`. That is the point; the exam asks about it.

**Drill:** Predict output:

```python
x = 1
def f(x=x):
    return x
x = 2
print(f())
```

Default values are bound at **definition** time.

### Day 10 — Recursion (light, exam-shaped)
**Exam objectives:** 4.1 (recursion)  
One recursive function. Know the base case or you loop until `RecursionError`.

**Build:** Recursively count open items, or a recursive menu depth counter, or factorial-style "days of fuel remaining" if you must. Keep it tiny.

```python
def count_open(items):
    if not items:
        return 0
    head, *tail = items
    return (0 if head["ok"] else 1) + count_open(tail)
```

**Drill:** Write recursive `sum_n(n)` with base `n <= 0`. Trace three frames on paper.

### Day 11 — Exception hierarchy
**Exam objectives:** 4.3  
`BaseException` → `Exception` → `ArithmeticError` / `LookupError` / …  
Know: `IndexError`, `KeyError`, `TypeError`, `ValueError`, `SystemExit`, `KeyboardInterrupt`.  
`KeyboardInterrupt` and `SystemExit` are **not** subclasses of `Exception`. That fact is exam bait.

**Build:** Nothing new to ship. Draw the tree in a comment block at the top of `brief_lib.py`. Force each of: `IndexError`, `KeyError`, `ValueError`, `TypeError` in the REPL and read the class MRO (`exc.__class__.__mro__`).

**Drill:** Which of these does `except Exception` catch? `KeyboardInterrupt`, `ValueError`, `SystemExit`, `IndexError`.

### Day 12 — `try` / `except`, branch order, propagation
**Exam objectives:** 4.4  
`try-except`, `except Exception`, order of branches (specific before general), exceptions crossing function boundaries.

**Build:** Wrap `int(input(...))` and list-index access.

```python
def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Not an integer.")
        return None
```

Add a function that does **not** catch, and a caller that does — so you see propagation.

**Drill:** This order is wrong. Fix it:

```python
try:
    ...
except Exception:
    ...
except ValueError:
    ...
```

### Day 13 — Integrate Week 1 data structures inside functions
Rehearse 3.1–3.4 under 4.x pressure.

**Build:** Move checklist logic behind functions: `add_item()`, `mark_ok()`, `render_report()`. Strings, lists, dicts, tuples all live *inside* functions now. Invalid keys raise `KeyError`; you catch at the UI layer.

### Day 14 — Weekend wrap, Git, exam simulation
**Build:**

- Two-file program runs from `python brief_builder.py`.
- Invalid input never crashes the process.
- README documents both week 1 and week 2, with example sessions.
- Branch `week2` merged to `main`. Tag `v0.2-week2`.

**Exam simulation (20 min):** Close the editor. On paper or a blank file, write from memory:

1. A `while` menu with `break` / `continue`.
2. A function with a default argument that returns a dict.
3. A `try/except` that catches `ValueError` then `Exception`.
4. A list comprehension that squares evens in `range(10)` (comprehensions *are* on the list syllabus).
5. The difference between `==` and `is`.
6. Why `except Exception` will not catch Ctrl-C.

Grade yourself harshly. Anything you had to look up becomes a flash card.

---

## Git practice baked into the two weeks

You asked for Git as well as Python. Treat the repo as the second exam.

| Habit | Rule |
| --- | --- |
| First commit | README + `.gitignore` + empty script. Not "working code." |
| Message style | Imperative, present: `Add while-menu for checklist` |
| Frequency | One commit per day minimum. Small diffs. |
| Branches | `week1`, `week2`. Merge with `--no-ff` so history stays readable. |
| Tags | `v0.1-week1`, `v0.2-week2` |
| Never | Commit `__pycache__`, secrets, or "asdf" messages |
| After merge | `git log --oneline --graph` should tell the story without the code |

If the remote is GitHub: push daily. That is the entire "cloud backup and portfolio" strategy this fortnight needs.

---

## What this pair of programs forces onto the exam

| Syllabus slice | Where it lives in the drills |
| --- | --- |
| Interpreter / compiler, lexis / syntax / semantics | Day 1 comments + README "how Python runs this file" |
| Literals, numeral systems, PEP 8 names | Days 1–2 |
| Operators, bitwise, booleans, casting, float accuracy | Day 2 |
| Console I/O, `sep` / `end` | Days 1 and 7 |
| `if` family, nesting | Day 3 |
| `while` / `for` / `range` / `else` on loops / `break` / `continue` / `pass` | Day 4 |
| Lists, slices, copy vs clone, matrices | Day 5 |
| Tuples vs lists, dict methods | Day 6 |
| Strings, escapes, methods | Day 7 |
| `def` / `return` / `None` / recursion / generators (aware) | Days 8, 10 |
| Arguments, defaults, scope, `global`, shadowing | Day 9 |
| Exception tree | Day 11 |
| `try/except` order and propagation | Day 12 |
| List comprehensions | Day 14 simulation + optional one-liner in the report |

File I/O, modules/`import` beyond your own file, OOP, and pip packages are **PCAP**, not PCEP. Do not wander there this fortnight. Curiosity is allowed; scope creep is how two-week plans die.

---

## Daily-life extensions (only after the exam slice works)

Once the checklist and brief builder run, you may add *one* real hook per week — not before:

- Dump the readiness report to a dated `.txt` (practice `open`/`with` as a preview of PCAP).
- Hard-code your actual kit list (fuel cans, meds, radio, water).
- Emit a three-bullet "morning brief" you could paste into a client note.

Resist APIs, GUIs, and frameworks. PCEP rewards boring, correct code.

---

## After these two weeks

1. Finish any unread Python Essentials 1 modules.
2. Sit a timed practice exam (OpenEDG practice test exists; third-party dumps are a waste of a CISSP's time).
3. Book PCEP-30-02 while the syntax is hot.
4. Next fortnight, if you want the associate rung: PCAP adds modules/packages, deeper exceptions, strings, OOP, comprehensions/lambdas/closures, and file I/O. Same 15-minute discipline, larger programs.

Two modest programs, fourteen commits, one syllabus. That is the entire brief.
