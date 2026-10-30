"""Personal Expense Tracker - a basic Python CLI project.

Demonstrates core Python: functions, dictionaries/lists, file handling
(CSV), input validation, and simple data summaries. No external libraries.
"""

import csv
import os
from datetime import date

DATA_FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


def add_expense(expenses, category, description, amount, expense_date=None):
    """Add one expense to the list and return it. Raises ValueError on bad amount."""
    amount = float(amount)
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    if not category.strip():
        raise ValueError("Category cannot be empty")
    expense = {
        "date": expense_date or date.today().isoformat(),
        "category": category.strip().title(),
        "description": description.strip(),
        "amount": round(amount, 2),
    }
    expenses.append(expense)
    return expense


def total_spent(expenses):
    """Return the total of all expenses."""
    return round(sum(e["amount"] for e in expenses), 2)


def summary_by_category(expenses):
    """Return a dict of category -> total spent, sorted by total (highest first)."""
    summary = {}
    for e in expenses:
        summary[e["category"]] = round(summary.get(e["category"], 0) + e["amount"], 2)
    return dict(sorted(summary.items(), key=lambda item: item[1], reverse=True))


def save_expenses(expenses, path=DATA_FILE):
    """Save expenses to a CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


def load_expenses(path=DATA_FILE):
    """Load expenses from a CSV file. Returns an empty list if the file doesn't exist."""
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [{**row, "amount": float(row["amount"])} for row in reader]


def print_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print(f"\n{'Date':<12}{'Category':<15}{'Description':<30}{'Amount':>10}")
    print("-" * 67)
    for e in expenses:
        print(f"{e['date']:<12}{e['category']:<15}{e['description']:<30}${e['amount']:>9.2f}")
    print("-" * 67)
    print(f"{'TOTAL':<57}${total_spent(expenses):>9.2f}\n")


def print_summary(expenses):
    summary = summary_by_category(expenses)
    if not summary:
        print("No expenses yet.")
        return
    print("\nSpending by category:")
    for category, total in summary.items():
        print(f"  {category:<15} ${total:>9.2f}")
    print()


def main():
    expenses = load_expenses()
    print("=== Personal Expense Tracker ===")
    while True:
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            try:
                category = input("Category (e.g. Food, Travel, Bills): ")
                description = input("Description: ")
                amount = input("Amount ($): ")
                expense = add_expense(expenses, category, description, amount)
                save_expenses(expenses)
                print(f"Added: {expense['category']} - ${expense['amount']:.2f}\n")
            except ValueError as err:
                print(f"Error: {err}\n")
        elif choice == "2":
            print_expenses(expenses)
        elif choice == "3":
            print_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
