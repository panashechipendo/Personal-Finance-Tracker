# Personal Finance Tracker - Project Roadmap

## Phase 1: Core Data Structure & Storage

### Data Format (CSV columns):
```
date,type,category,description,amount,balance
2024-01-15,income,salary,Monthly salary,2500.00,2500.00
2024-01-16,expense,food,Groceries,85.50,2414.50
2024-01-17,expense,transport,Bus fare,12.00,2402.50
```

### Functions to implement:
- `add_transaction()` - Add income/expense
- `load_data()` - Read from CSV file
- `save_data()` - Write to CSV file

## Phase 2: Budget Management

### Budget storage (separate CSV or JSON):
```
category,monthly_budget,current_spent
food,300.00,185.50
transport,150.00,45.00
entertainment,100.00,0.00
```

### Functions:
- `set_budget()` - Set monthly budget for categories
- `calculate_budget_remaining()` - Check remaining budget
- `check_budget_alerts()` - Warn when approaching limits

## Phase 3: Reporting & Analysis

### Functions:
- `generate_report()` - Monthly/weekly summaries
- `category_breakdown()` - Spending by category
- `export_data()` - Export filtered data to CSV

## Phase 4: User Interface

### Main menu structure:
1. Add transaction
2. View current balance
3. Set/view budgets
4. Generate reports
5. Export data
6. Exit

## Key Design Decisions

### File Structure:
- `transactions.csv` - All transactions
- `budgets.json` - Budget settings
- `project.py` - Main program
- `test_project.py` - Tests

### Data Validation:
- Ensure amounts are positive numbers
- Validate dates
- Check category names
- Handle file errors gracefully

### Testing Strategy:
- Test transaction adding with valid/invalid data
- Test budget calculations
- Test file operations

### Future Expansion Ideas:
- Add data visualization with matplotlib
- Implement recurring transactions
- Add investment tracking
- Create web interface with Flask

## CLI Tool Enhancement

### Main Menu Display:
```
=== Personal Finance Tracker ===
1. Add Transaction
2. View Balance
3. Set Budget
4. View Budget Status
5. Generate Report
6. Export Data
7. Exit

Choose an option: 
```

### User Experience Flow:
```
$ python project.py

Choose an option: 1
Enter transaction type (income/expense): expense
Enter category: food
Enter description: Lunch at restaurant
Enter amount: 25.50
✓ Transaction added successfully!

Current balance: $1,234.50
```

### Required Functions (CS50P Compliance):
1. `add_transaction()` - Handle user input and data validation
2. `generate_report()` - Create formatted output of financial data
3. `calculate_budget_remaining()` - Calculate and display budget status

### Implementation Notes:
- Keep all functions in `project.py` at the same indentation level
- Create comprehensive tests in `test_project.py`
- Handle edge cases and user input errors gracefully
- Use clear prompts and feedback messages for better user experience