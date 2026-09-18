# Week 1 resilience — session notes

For a future session in this folder: start here, then open the exercise program in Obsidian. Do not rediscover the layout from git history unless these notes look stale.

## Review protocol (do not skip)

The operator builds the day's slice, then asks for a look only after it has passed what they can see. Do **not** rewrite their drill unprompted. Do **not** implement Days 7–14 for them.

After a requested review:

1. Read `resilience_check.py` (and `matrix.py` if touched) against that day's **Pass if you can** list in the Obsidian program.
2. Append a review to `PROGRESS.md` (grade, pass-list marks, short recommendations). Update the day log and running totals.
3. Tell them the grade and the recommendations in chat. Keep the punch list short.

`PROGRESS.md` is gitignored on purpose so `git add -A` does not commit grades. `NOTES.md` may be committed; it is orientation, not a gradebook.

## Where the instructions live

- Exercise program (canonical): `~/Projects/bpelleti/01 - Projects/PCEP Prep/PCEP_2_Week_Exercise_Program.md`
- ANSI band pattern: `~/Projects/bpelleti/01 - Projects/PCEP Prep/ANSI Colors.md`
- Git close-out: `~/Projects/bpelleti/01 - Projects/PCEP Prep/Github Common commands.md`
- This folder is the Week 1 *program* (`resilience_check.py`). Calendar weeks 1–2 of the drill both land here. `../week2_brief/` is the functions/exceptions program and starts after Day 14.

## Current code (catch-up review 2026-09-18, uncommitted)

Files:

- `resilience_check.py` — the checklist. Menu, list-of-dicts, fuel math, color bands.
- `matrix.py` — Day 5 extra (3×3 diagonal). Leave it; it is exam-shaped.

What already works (after catch-up):

- Banner, `user` (operator), date, month — Add uses `name` for the item only
- Gallons on hand / required / shortfall, `fuel_ok`
- Kit y/n → `kit_ok` (separate from the item list)
- `while True` menu: Add / List / Remove / Quit / `elif done == 5: pass`
- `kit_items` is a list of dicts `{"name", "qty": int, "ok": bool}`
- List and closing report walk `.items()` into a line
- Day 3 bands: both → green, either → yellow, neither → red + hurricane-season nest
- Extra credit: `recommended` string list with slice, `sorted`, and `[:]` clone

Still open (not Day 10+ work):

1. **`category` is joined on the report** (`" | ".join(category)`). Legend only. Day 10 later puts a `"category"` key on each row and checks `in category`.
2. **Clone without alias.** Extra credit uses `recommended` (strings): slice, `sorted`, clone then `append`. Still missing `b = recommended` vs `b = recommended[:]` printed side by side after a mutate.
3. **Remove** has no bounds check. Day 12: `if`/`continue`, not `try/except`.
4. **ANSI is on the status sentence only.** Day 9: pad text to `WIDTH` then wrap codes.
5. **`kit_ok` is still a y/n**, not derived from items. Day 13.
6. Repo `README.md` is empty. `.gitignore` currently only ignores `PROGRESS.md`. Day 14 wrap fills both.

## Original intent (do not break)

- PCEP-30-02 practice, not a product.
- ~15 minutes per weekday. Incomplete features are valid commits.
- Week 1 (through Day 14) is Blocks 1–3: types, operators, `if`, loops, list/dict/tuple/string. **User-defined functions are not required.** One optional `band()` copy from the ANSI note is the only `def` that belongs here; it is a preview of Week 2.
- No `try/except`, no `open()`, no modules beyond the stdlib you already use, no pip, no GUI, no API.
- Fuel stays its own axis (Day 2). Do not delete gallons just because POWER items exist.
- Color bands stay the Day 3 rule: fuel **and** kit → green; either → yellow; neither → red; nest hurricane season on red.
- Stay on git branch `week1` until Day 14. Do not merge after Day 7.

## What the extra week is for

Day 7 in the original plan was the entire string/report slice. That is too thin for Block 3 (25% of the exam) and the current report is unreadable. Calendar week 2 stays in this folder and does two things:

1. **Report formatting** — `center` / `ljust` / `rjust` or f-string align, `WIDTH = 60`, separators, full-width ANSI band, title-case names, `" | ".join(category)`.
2. **Granular kit rows** — each item has category, on-hand qty, required need, condition `ok`. Readiness is computed at item, category, and overall levels.

Daily slices are in the Obsidian program under **Week 1 Extension (Days 8–14)**.

## Target item schema (Day 10+)

```python
{
    "name": "5-gal fuel can",   # str, title-cased on add
    "category": "POWER",        # must be in the category tuple
    "qty": 2,                   # int, on hand
    "need": 4,                  # int, required
    "ok": False,                # bool, works / not expired
}
```

- Item READY ⇔ `qty >= need and ok`
- SHORT ⇔ `qty < need` (and ok)
- FAULT ⇔ `not ok` (FAULT wins if both)
- Category line: `ready / total` for that category, including `0/0` if none logged
- `kit_ok` ⇔ `len(items) > 0 and ready_count == len(items)`
- `fuel_ok` unchanged: `gallons_on_hand >= gallons_required`

Starter rows to type during Add (one per category at minimum). Do not hard-code the list until Add works.

| category | name | need |
| --- | --- | --- |
| POWER | 5-gal fuel can | 4 |
| POWER | Generator oil (qt) | 2 |
| POWER | AA batteries | 12 |
| POWER | Flashlight / lantern | 2 |
| WATER | Stored water (gal) | 14 |
| WATER | Purification tablets | 1 |
| COMMS | NOAA weather radio | 1 |
| COMMS | Charged power bank | 2 |
| MED | First aid kit | 1 |
| MED | Prescription days on hand | 7 |

## Target report (Day 14 definition of done)

`WIDTH = 60`. Pad the *text* to WIDTH, then wrap ANSI. Color codes have string length but do not take terminal columns.

```
                    NAVARRE RESILIENCE CHECK
Operator: Bob               Date: 2026-09-18        Month: 9
Categories: POWER | WATER | COMMS | MED
------------------------------------------------------------
FUEL   on hand:  3   required:  5   shortfall:  2   SHORT
------------------------------------------------------------
#  CAT    ITEM                      HAVE NEED GAP  STATUS
1  POWER  5-Gal Fuel Can               2    4   2  OPEN
2  WATER  Stored Water (Gal)          14   14   0  READY
------------------------------------------------------------
POWER 1/4  |  WATER 1/1  |  COMMS 0/0  |  MED 0/0
Items ready: 1/2 (50%)
------------------------------------------------------------
[======= AMBER — finish the kit or get more gas =======]
```

Menu 2 (List) should use the same columns, numbered, so Remove by index matches what you see.

## Resume checklist for a new session

1. Read this file and `PROGRESS.md` (last grade, catch-up punch list, day log).
2. Open the day's section of the Obsidian program.
3. `git log --oneline -5` and `git status` — expect branch `week1`.
4. If they are catching up Days 1–6, they work in `resilience_check.py` only. If they called a day done, review and write `PROGRESS.md`.
5. They commit their code: `Add Day N: ...` then `git push`. Do not stage `PROGRESS.md`.

Day 7 is the next original day (strings + first formatted report). Days 8–14 are the extension. Week 2 brief builder does not start until Day 14 is merged and tagged `v0.1-week1`.
