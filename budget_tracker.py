# ============================================================
#  FAC ACADEMY - Python & Django Programme
#  Week 1, Session 5 - Mini Project
#  Project: Interactive Personal Budget Tracker
#  Author : Tito Kilonzo
# ============================================================


def get_positive_float(prompt):
    """Prompt the user until a valid positive number is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  Amount cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 5000).")


def main():
    print("=" * 55)
    print("        PERSONAL BUDGET TRACKER - FAC ACADEMY")
    print("=" * 55)

    # REQUIREMENT 1: Accept monthly income (float)
    print("\nINCOME")
    monthly_income = get_positive_float("  Enter your monthly income (KES): ")

    # REQUIREMENT 2: Accept 5 expense categories with amounts
    print("\nEXPENSES - Enter amounts for each category")
    expense_categories = [
        "Rent / Housing",
        "Food & Groceries",
        "Transport",
        "Utilities (Water/Electricity)",
        "Other / Miscellaneous",
    ]

    expenses = {}
    for i, category in enumerate(expense_categories, start=1):
        amount = get_positive_float(f"  {i}. {category}: KES ")
        expenses[category] = amount

    # REQUIREMENT 3: Calculate total expenses and savings
    total_expenses = sum(expenses.values())
    savings = monthly_income - total_expenses

    # REQUIREMENT 4: Determine savings percentage of income
    if monthly_income > 0:
        savings_percent = (savings / monthly_income) * 100
    else:
        savings_percent = 0.0

    # REQUIREMENT 5: Display formatted budget summary
    print("\n" + "=" * 55)
    print("               BUDGET SUMMARY")
    print("=" * 55)
    print(f"  {'Monthly Income':<30} KES {monthly_income:>10,.2f}")
    print("-" * 55)
    print("  EXPENSES BREAKDOWN:")
    for category, amount in expenses.items():
        print(f"    {category:<28} KES {amount:>10,.2f}")
    print("-" * 55)
    print(f"  {'Total Expenses':<30} KES {total_expenses:>10,.2f}")
    print(f"  {'Savings':<30} KES {savings:>10,.2f}")
    print(f"  {'Savings Rate':<30} {savings_percent:>10.1f}%")
    print("=" * 55)

    # REQUIREMENT 6: Show SURPLUS or DEFICIT message
    if savings >= 0:
        print(f"\n  SURPLUS - You are saving KES {savings:,.2f} this month.")
    else:
        print(f"\n  DEFICIT - You are overspending by KES {abs(savings):,.2f}.")
        print("  Consider reducing your expenses.")

    print("\n" + "=" * 55)
    print("  Budget summary complete.")
    print("=" * 55 + "\n")


# Entry point
if __name__ == "__main__":
    main()