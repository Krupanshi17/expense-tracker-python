from datetime import datetime

def get_valid_amount():
    while True:
        amount=input("Enter amount: ").strip()
        try:
            amount=float(amount)
            if amount<=0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    
def get_valid_category():
    while True:
        category=input("Enter category: ").strip()
        if category:
            return category
        print("Category cannot be empty.")



def get_expense_date():
    choice=input("Use today's date? (y/n): ").strip().lower()
    if choice=='y':
        return datetime.today().strftime("%Y-%m-%d")

    while True:
        date_input=input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


#Collects expense details from user and returns an expense dictionary.
def add_expense():
    date=get_expense_date()
    category=get_valid_category()
    amount=get_valid_amount()
    note=input("Enter note (optional): ").strip()

    return {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

