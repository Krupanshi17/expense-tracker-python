from storage import load_expenses, save_expenses
from utils import add_expense
from reports import (
    view_all_expenses,
    calculate_total,
    filter_by_category,
    monthly_report,
    plot_monthly_expenses
)

def show_menu():
    print("\nExpense Tracker Menu")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Expenses by Category")
    print("5. Monthly Report")
    print("6. Monthly Expense Chart")
    print("7. Exit")

def main():
    expenses=load_expenses()

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice=="1":
            new_expense=add_expense()
            expenses.append(new_expense)
            save_expenses(expenses)
            print("Expense Added Successfully!")

        elif choice=="2":
            view_all_expenses(expenses)

        elif choice=="3":
            total=calculate_total(expenses)
            print(f"\nTotal Spending: ₹{total:.2f}")

        elif choice=="4":
            category = input("Enter category to search: ").strip()
            filtered=filter_by_category(expenses, category)
            if not filtered:
                print(f"\nNo expenses found for category: {category}")
            else:
                view_all_expenses(filtered)

        elif choice=="5":
            report=monthly_report(expenses)
            if not report:
                print("\nNo expenses available for monthly report.")
            else:
                print("\n Monthly Report")
                for month, total in sorted(report.items()):
                    print(f"{month} : ₹{total:.2f}")
        
        elif choice=="6":
            plot_monthly_expenses(expenses)

        elif choice=="7":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__=="__main__":
    main()
