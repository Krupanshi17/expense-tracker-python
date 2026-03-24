import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#It will show user the expenses he has done
def view_all_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\nAll Expenses")
    for idx, expense in enumerate(expenses, start=1):
        print(
            f"{idx}. Date: {expense['date']} | "
            f"Category: {expense['category']} | "
            f"Amount: {expense['amount']} | "
            f"Note: {expense['note']}"
        )

#It will calculate the total amount spent by user
def calculate_total(expenses):
    if not expenses:
        return 0.0
    total=0.0
    for expense in expenses:
        total+=expense.get('amount',0.0)
    return total

#It will filter expenses and its details by category
def filter_by_category(expenses, category):
    category=category.lower()
    filtered=[]

    for expense in expenses:
        if expense.get("category", "").lower() == category:
            filtered.append(expense)

    return filtered

#It will generate a monthly report of the total expenses
"""
Groups expenses by month and calculates total spending per month.
"""
def monthly_report(expenses):

    report={}

    for expense in expenses:
        date=expense.get("date", "")
        month=date[:7]  # YYYY-MM

        amount=expense.get("amount", 0)

        if month in report:
            report[month]+=amount
        else:
            report[month]=amount

    return report


def plot_monthly_expenses(expenses):
    report=monthly_report(expenses)

    if not report:
        print("No data available to plot.")
        return

    months=list(report.keys())
    totals=list(report.values())

    plt.figure()
    plt.bar(months, totals)
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.title("Monthly Expense Report")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


