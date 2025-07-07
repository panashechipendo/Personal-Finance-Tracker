import csv
import sys

options = ["Add Transaction", "View Balance", "Set Budget", "View Budget Status", "Generate Report", "Export Data", "Exit"]

def main():
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    option = input("Select an Option: ")
    while True:
        try:
            user_input = input("Choose a number from the options: ")
            if options[int(user_input) - 1]:
                if user_input == "1":
                    add_transaction()
                elif user_input == "2":
                    load_data()
        except IndexError:
            print("No option at that number")
            sys.exit(1)
        except ValueError:
            print("Not a valid input")



    
    

def add_transaction():
    ...

def load_data():
    ...

def savedata():
    ...

def set_budget():
    ...

def calculate_budget_remaining():
    ...

def check_budget_alerts():
    ...


if __name__ == "__main__":
    main()