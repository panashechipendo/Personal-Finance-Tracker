import csv
import sys

options = ["Add Transaction", "View Balance", "Set Budget", "View Budget Status", "Generate Report", "Export Data", "Exit"]

def main():
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    

def add_transaction():
    ...

def load_data():
    ...

def savedata():
    ...


if __name__ == "__main__":
    main()