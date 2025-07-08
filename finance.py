from tabulate import tabulate
from openpyxl import Workbook
import csv
import sys
import datetime


options = ["Add Transaction", "View Balance", "Set Budget", "View Budget Status", "Generate Report", "Export Data", "Exit"]

def display_menu():
    print("\n" + "="*30)
    print("       Finance Tracker")
    print("="*30)
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    print("="*30)

def main():
    while True:
        display_menu()
        try:
            user_input = input("Choose a number from the options: ")
            choice = int(user_input)

            if choice < 1 or choice > len(options):
                print("Please enter a number between 1 and 7")
                continue
                
            if choice == 1:
                add_transaction()
            elif choice == 2:
                view_balance()
            elif choice == 3:
                set_budget()
            elif choice == 4: 
                view_budget_status()
            elif choice == 5:
                generate_report()
            elif choice == 6:
                export_data()
            elif choice == 7:
                print("Thank you for using Finance Tracker!")
                sys.exit(0)
        except ValueError:
            print("Not a valid input")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def add_transaction():
    data = load_data()
    budget_data = load_budget_data()
    balance = 0
    if len(budget_data) > 0:
        for entry in budget_data:
            balance += int(entry["monthly_budget"])
    else: 
        balance = 0

    while True:
        try:
            today = datetime.date
            transaction = input("Enter transaction types (income/expense): ")
            if transaction == "income" or transaction == "expense":
                category = input("Enter category: ")  
            else:
                 continue
            

            description = input("Enter description: ")
            amount = input("Enter amount: ")
            

            if transaction == "income":
                balance = int(balance) + int(amount)
            elif transaction == "expense" and int(balance) > 0:
                balance = int(balance) - int(amount)
                check_budget_alerts()
            else:
                balance = balance
          
            savedata(today.today(), transaction, category, description, amount, balance)
            print("✔️ Transaction added successfully!")
            print()
            view_balance()
            break
        except KeyboardInterrupt:
            print("Thank you for using Finance Tracker!")
        except ValueError:
            print("Thats an invalid input")
            continue
            

def view_balance():
    data = load_data()
    if len(data) > 0:
        balance = data[-1]["balance"]
    else: 
        balance = 0

    print(f"Current balance: {balance}")

def view_budget_status():
    budget = load_budget_data()
    if len(budget) == 0:
        print("Cant display budget that's not defined")
        return
    
    print(tabulate(budget, headers="keys", tablefmt="grid"))

def generate_report():
    data = load_data()
    if len(data) > 0:
        print(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        print("No Transaction History")

def export_data():
    data = load_data()
    if len(data) == 0:
        print("Can't export an empty file!")
        return
    formatted  = input("Please select a format(.xlsx(excel), .csv(comma separated value))")
    if formatted == ".xlsx" or formatted == "excel":
        wb = Workbook()
        ws = wb.active
        ws.title = "Transactions"
        ws["A1"] = "Date"
        ws["B1"] = "types"
        ws["C1"] = "Category"
        ws["D1"] = "Description"
        ws["E1"] = "Amount"
        ws["F1"] = "Balance"

        for entry in data:
            ws.append(
                [
                    entry["date"],
                    entry["types"],
                    entry["category"],
                    entry["description"],
                    entry["amount"],
                    entry["balance"]
                ]
            )
        wb.save("output.xlsx")
        print("File Exported!: output.xlsx")
    elif formatted == ".csv":
        with open("output.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "types", "category", "description", "amount", "balance"])
            writer.writeheader()
            for entry in data:
                writer.writerow(entry)
        print("File exported! output.csv")


def load_data():
        data = []
        with open("transactions.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(
                    {
                        "date": row["date"],
                        "types": row["types"],
                        "category": row["category"],
                        "description": row["description"],
                        "amount": row["amount"],
                        "balance": row["balance"]
                    }
                )
        return data

def load_budget_data():
    budgets = []
    with open("budgets.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            budgets.append({
                "category": row["category"],
                "monthly_budget": int(row["monthly_budget"])
            })
    return budgets

def savedata(date, types, category, description, amount, balance):
    with open("transactions.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "types", "category", "description", "amount", "balance"])
        writer.writerow(
            {
                "date": date,
                "types": types,
                "category": category,
                "description": description,
                "amount": amount,
                "balance": balance
            }
        )

def set_budget():
    while True:
        try:
            category = input("Enter budget category: ")
            monthly = int(input("Enter monthly budget: "))
            with open("budgets.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["category", "monthly_budget"])
                writer.writerow(
                    {
                        "category": category,
                        "monthly_budget": monthly,
                    }
                )
            break
        except ValueError:
            print("invalid input")
            continue
        except KeyboardInterrupt:
            print("Thank you for using finance tracker!")

def calculate_budget_remaining():
    budgets = load_budget_data()
    transactions = load_data()

    results = []

    for budget in budgets:
        category = budget["category"]
        monthly_limit = budget["monthly_budget"]

        category_expenses = [t for t in transactions if t["types"] == "expense" and t["category"] == category]

        total_spent = sum(int(expense["amount"]) for expense in category_expenses)

        remaining = monthly_limit - total_spent

        results.append({
            "category": category,
            "monthly_budget": monthly_limit,
            "current_spent": total_spent,
            "remaining": remaining
        })

    return results

def check_budget_alerts():
    budget_remain = calculate_budget_remaining()
    if budget_remain:
        for remain in budget_remain:
            total = remain["monthly_budget"]
            if int(remain["remaining"]) <= 0:
                print(f"Alert!: {remain["category"]}'s budget has been reached/exceeded: ${remain["remaining"]}")
                return True
            elif int(remain["remaining"]) <= (0.1 * total) and int(remain["remaining"]) > 0:
                print(f"WARNING: {remain["category"]}'s budget is about to be reached: ${remain["remaining"]}")
                return True
            else: 
                return False



if __name__ == "__main__":
    main()