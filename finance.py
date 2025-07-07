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
                
            if user_input == "1":
                add_transaction()
            elif user_input == "2":
                view_balance()
            elif user_input == "3":
                set_budget()
            elif user_input == "4": 
                view_budget_status()
            elif user_input == "5":
                generate_report()
            elif user_input == "6":
                export_data()
            elif user_input == "7":
                    print("Thank you for using Finance Tracker!")
                    sys.exit(0)
        except ValueError:
            print("Not a valid input")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def add_transaction():
    data = load_data()
    balance = data[-1]["balance"]

    while True:
        try:
            today = datetime.date
            transaction = input("Enter transaction type (income/expense): ")
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
          
            savedata(today.today(), transaction, category, description, amount, balance)
            print("✔️ Transaction added successfully!")
            print()
            print(view_balance())
            break
        except KeyboardInterrupt:
            print("Thank you for using Finance Tracker!")
        except ValueError:
            print("Thats an invalid input")
            continue
            

def view_balance():
    ...

def view_budget_status():
    ...

def generate_report():
    ...

def export_data():
    ...

def load_data():
        data = []
        with open("transactions.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(
                    {
                        "date": row["date"],
                        "type": row["type"],
                        "category": row["category"],
                        "description": row["description"],
                        "amount": row["amount"],
                        "balance": row["balance"]
                    }
                )
        return data

def savedata(date, type, category, description, amount, balance):
    with open("transactions.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "type", "category", "description", "amount", "balance"])
        writer.writerow(
            {
                "date": date,
                "type": type,
                "category": category,
                "description": description,
                "amount": amount,
                "balance": balance
            }
        )

def set_budget():
    ...

def calculate_budget_remaining():
    ...

def check_budget_alerts():
    ...


if __name__ == "__main__":
    main()