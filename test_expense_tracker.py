"""Tests for the Expense Tracker. Uses only the built-in unittest module.

Run with:  python -m unittest discover -v
"""

import os
import tempfile
import unittest

from expense_tracker import (
    add_expense,
    load_expenses,
    save_expenses,
    summary_by_category,
    total_spent,
)


class TestExpenseTracker(unittest.TestCase):
    def test_add_expense(self):
        expenses = []
        item = add_expense(expenses, "food", "Lunch", 12.50, "2026-10-30")
        self.assertEqual(len(expenses), 1)
        self.assertEqual(item["category"], "Food")
        self.assertEqual(item["amount"], 12.50)

    def test_add_expense_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            add_expense([], "Food", "Bad", -5)

    def test_add_expense_rejects_empty_category(self):
        with self.assertRaises(ValueError):
            add_expense([], "  ", "Bad", 10)

    def test_total_spent(self):
        expenses = []
        add_expense(expenses, "Food", "Lunch", 10)
        add_expense(expenses, "Travel", "Bus", 2.50)
        self.assertEqual(total_spent(expenses), 12.50)

    def test_summary_by_category(self):
        expenses = []
        add_expense(expenses, "Food", "Lunch", 10)
        add_expense(expenses, "Food", "Dinner", 20)
        add_expense(expenses, "Bills", "Internet", 50)
        summary = summary_by_category(expenses)
        self.assertEqual(summary["Food"], 30)
        self.assertEqual(summary["Bills"], 50)

    def test_save_and_load_round_trip(self):
        expenses = []
        add_expense(expenses, "Food", "Lunch", 12.50, "2026-10-30")
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "expenses.csv")
            save_expenses(expenses, path)
            loaded = load_expenses(path)
        self.assertEqual(loaded, expenses)


if __name__ == "__main__":
    unittest.main()
