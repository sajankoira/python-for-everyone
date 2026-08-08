"""
PROJECT 7: Expense Tracker (CSV + Data Analysis intro)
"""
import csv
import os
from datetime import datetime
from collections import defaultdict

FILE = "expenses.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "note"])

def add_expense(category, amount, note=""):
    init_file()
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount, note])
    print(f"Added {category} - {amount}")

def view_expenses():
    init_file()
    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        total = 0
        by_cat = defaultdict(float)
        print("\n--- All Expenses ---")
        for row in reader:
            print(f"{row['date']} | {row['category']:10} | Rs.{row['amount']:6} | {row['note']}")
            total += float(row["amount"])
            by_cat[row["category"]] += float(row["amount"])
        print(f"\nTotal Spent: Rs.{total}")
        print("By Category:")
        for cat, amt in by_cat.items():
            print(f"  {cat}: Rs.{amt}")

if __name__ == "__main__":
    print("💰 Expense Tracker")
    while True:
        print("\n1. Add 2. View 3. Exit")
        ch = input("Choice: ")
        if ch == "1":
            cat = input("Category (Food/Travel/Shopping/Other): ") or "Other"
            amt = input("Amount: ")
            note = input("Note: ")
            try:
                add_expense(cat, float(amt), note)
            except ValueError:
                print("Invalid amount")
        elif ch == "2":
            view_expenses()
        elif ch == "3":
            break
