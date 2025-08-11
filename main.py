import csv
import os
from datetime import datetime

FILE_NAME = "transactions.csv"

def init_file():
    """Create CSV file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amount", "Description"])

def add_transaction(t_type, amount, description):
    """Add income or expense to the CSV file."""
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), t_type, amount, description])
    print(f"{t_type} of ₹{amount} added successfully.")

def view_transactions():
    """Display all transactions."""
    if not os.path.exists(FILE_NAME):
        print("No transactions found.")
        return
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def calculate_balance():
    """Calculate current balance."""
    if not os.path.exists(FILE_NAME):
        return 0
    balance = 0
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Type"].lower() == "income":
                balance += float(row["Amount"])
            elif row["Type"].lower() == "expense":
                balance -= float(row["Amount"])
    return balance

def menu():
    """Display the main menu."""
    init_file()
    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            description = input("Enter description: ")
            add_transaction("Income", amount, description)

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            description = input("Enter description: ")
            add_transaction("Expense", amount, description)

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            print(f"Current Balance: ₹{calculate_balance():.2f}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
