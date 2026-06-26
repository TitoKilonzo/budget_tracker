# FAC Academy — Week 1 Mini Project
## Interactive Personal Budget Tracker

A beginner Python project built as part of the **FAC Academy Python & Django Programme**, Week 1, Session 5.

---

## 📋 Project Overview

This command-line program helps users track their monthly income and expenses, calculates savings, and displays a formatted budget summary — integrating all Week 1 Python concepts.

---

## ✅ Requirements Met

| # | Requirement | Implementation |
|---|---|---|
| 1 | Accept monthly income (float) | `get_positive_float()` with validation |
| 2 | Accept 5 expense categories + amounts | Loops through a predefined category list |
| 3 | Calculate total expenses & savings | `sum()` + subtraction |
| 4 | Savings % of income | `(savings / income) * 100` |
| 5 | Formatted budget summary (f-strings) | Aligned columns with `,.2f` number format |
| 6 | SURPLUS / DEFICIT message | Conditional check on savings value |

---

## 🛠 Setup & Installation

### Prerequisites

- **Python 3.6 or higher** installed on your machine

### Check Python Version

```bash
python --version
# or
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

---

## 🚀 How to Run

### Step 1 — Extract the ZIP

Unzip the downloaded file to a folder of your choice.

```bash
unzip budget_tracker.zip
cd budget_tracker
```

### Step 2 — Run the Program

```bash
python budget_tracker.py
```

> On some systems (Linux/macOS) you may need to use `python3`:
> ```bash
> python3 budget_tracker.py
> ```

### Step 3 — Follow the Prompts

```
=======================================================
        PERSONAL BUDGET TRACKER — FAC ACADEMY
=======================================================

📥  INCOME
  Enter your monthly income (KES): 75000

📤  EXPENSES  (enter 5 categories)
  1. Rent / Housing: KES 25000
  2. Food & Groceries: KES 12000
  3. Transport: KES 4500
  4. Utilities (Water/Electricity): KES 2800
  5. Other / Miscellaneous: KES 3200
```

---

## 📊 Sample Output

```
=======================================================
               BUDGET SUMMARY
=======================================================
  Monthly Income                 KES  75,000.00
-------------------------------------------------------
  EXPENSES BREAKDOWN:
    Rent / Housing               KES  25,000.00
    Food & Groceries             KES  12,000.00
    Transport                    KES   4,500.00
    Utilities (Water/Electricity) KES   2,800.00
    Other / Miscellaneous        KES   3,200.00
-------------------------------------------------------
  Total Expenses                 KES  47,500.00
  Savings                        KES  27,500.00
  Savings Rate                         36.7%
=======================================================

  ✅  SURPLUS — You are saving KES 27,500.00 this month!
=======================================================
```

---

## 🔒 Edge Cases Handled

- **Non-numeric input** — prompts the user to re-enter (no crash)
- **Negative amounts** — rejected with a warning message
- **Zero income** — savings rate defaults to 0% safely

---

## 📁 File Structure

```
budget_tracker/
├── budget_tracker.py   # Main program
└── README.md           # This file
```

---

## 👤 Author

**Tito Kilonzo**
FAC Academy — Python & Django Programme, Week 1
