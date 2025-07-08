import csv
import os

from finance import (
    load_data, load_budget_data, savedata, 
    calculate_budget_remaining
)


def test_load_data_empty():
    if os.path.exists("transactions.csv"):
        os.remove("transactions.csv")
    
    data = load_data()
    assert data == []


def test_load_data_with_data():
    with open("transactions.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "types", "category", "description", "amount", "balance"])
        writer.writeheader()
        writer.writerow({"date": "2024-01-01", "types": "income", "category": "SALARY", "description": "Pay", "amount": "1000", "balance": "1000"})
    
    data = load_data()
    assert len(data) == 1
    assert data[0]["types"] == "income"


def test_load_budget_data_empty():
    if os.path.exists("budgets.csv"):
        os.remove("budgets.csv")
    
    budgets = load_budget_data()
    assert budgets == []


def test_savedata():
    if os.path.exists("transactions.csv"):
        os.remove("transactions.csv")
    
    load_data()  # Creates file
    savedata("2024-01-01", "income", "SALARY", "Test", "1000", "1000")
    
    data = load_data()
    assert len(data) == 1
    assert data[0]["amount"] == "1000"


def test_calculate_budget_remaining_empty():
    if os.path.exists("budgets.csv"):
        os.remove("budgets.csv")
    
    result = calculate_budget_remaining()
    assert result == []


# Run tests
if __name__ == "__main__":
    test_load_data_empty()
    test_load_data_with_data()
    test_load_budget_data_empty()
    test_savedata()
    test_calculate_budget_remaining_empty()
    print("All tests passed!")