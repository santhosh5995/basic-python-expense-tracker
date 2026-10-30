# Basic Python Project — Personal Expense Tracker

A simple command-line expense tracker written in **pure Python** — no external libraries to install. It is a beginner-friendly project that demonstrates the Python fundamentals every job description asks for.

## What it does

- **Add expenses** with a category, description, and amount (with input validation)
- **View all expenses** in a clean table with a running total
- **See spending by category** so you know where your money goes
- **Saves everything to a CSV file** (`expenses.csv`), so your data is still there when you run it again

## Python concepts used

- Functions and return values
- Lists and dictionaries
- File handling with the built-in `csv` module
- Error handling (`try` / `except`, raising `ValueError`)
- Sorting and aggregating data
- A menu-driven `main()` loop
- Unit testing with the built-in `unittest` module

## How to run

```bash
python expense_tracker.py
```

Then follow the menu:

```text
=== Personal Expense Tracker ===
1. Add expense
2. View all expenses
3. View summary by category
4. Exit
```

Example session:

```text
Choose an option (1-4): 1
Category (e.g. Food, Travel, Bills): Food
Description: Lunch
Amount ($): 12.50
Added: Food - $12.50
```

## How to run the tests

```bash
python -m unittest discover -v
```

All 6 tests pass: adding expenses, validation errors, totals, category summaries, and saving/loading the CSV file.

## Project structure

```text
basic-python-expense-tracker/
├── expense_tracker.py        # the app (add, view, summarize, save/load)
├── test_expense_tracker.py   # 6 unit tests
└── README.md
```

## Ideas to extend it

- Filter expenses by month
- Set a monthly budget and warn when you go over it
- Export the category summary as a chart

---

Built by Santhosh Reddy Angiti as a Python fundamentals portfolio project.
