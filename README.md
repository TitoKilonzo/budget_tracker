# FAC Academy - Week 1 Mini Project
# Interactive Personal Budget Tracker

A beginner Python project built as part of the FAC Academy Python & Django Programme,
Week 1, Session 5.

---

## Project Overview

This command-line program accepts a user's monthly income and five expense categories,
calculates savings, and displays a formatted budget summary with a SURPLUS or DEFICIT result.

---

## Requirements Met

| # | Requirement                        | Implementation                        |
|---|------------------------------------|---------------------------------------|
| 1 | Accept monthly income (float)      | get_positive_float() with validation  |
| 2 | Accept 5 expense categories        | Loop through predefined category list |
| 3 | Calculate total expenses & savings | sum() and subtraction                 |
| 4 | Savings percentage of income       | (savings / income) * 100              |
| 5 | Formatted budget summary           | f-strings with aligned columns        |
| 6 | SURPLUS or DEFICIT message         | Conditional check on savings value    |

---

## Prerequisites

- Python 3.6 or higher

Check your Python version:

    python --version

If Python is not installed, download it from https://www.python.org/downloads/

---

## Setup

1. Unzip the archive:

    unzip budget_tracker.zip
    cd budget_tracker

2. Run the program:

    python budget_tracker.py

   On Linux or macOS you may need:

    python3 budget_tracker.py

---

## Usage

Follow the prompts in the terminal:

    -------------------------------------------------------
            PERSONAL BUDGET TRACKER - FAC ACADEMY
    -------------------------------------------------------

    INCOME
      Enter your monthly income (KES): 75000

    EXPENSES - Enter amounts for each category
      1. Rent / Housing: KES 25000
      2. Food & Groceries: KES 12000
      3. Transport: KES 4500
      4. Utilities (Water/Electricity): KES 2800
      5. Other / Miscellaneous: KES 3200

    -------------------------------------------------------
                   BUDGET SUMMARY
    -------------------------------------------------------
      Monthly Income                 KES  75,000.00
      ...
      SURPLUS - You are saving KES 27,500.00 this month.

---

## Edge Cases Handled

- Non-numeric input: user is prompted to re-enter, program does not crash
- Negative amounts: rejected with a warning message
- Zero income: savings rate defaults to 0% safely

---

## File Structure

    budget_tracker/
    |-- budget_tracker.py   Main program
    |-- README.md           This file

---

## Author

Tito Kilonzo
FAC Academy - Python & Django Programme, Week 1
