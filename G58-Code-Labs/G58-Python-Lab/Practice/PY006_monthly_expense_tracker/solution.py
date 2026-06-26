# Variable: monthly income
income = 50000

# Variables: monthly expenses
rent = 15000
groceries = 6000
electricity = 1800
internet = 1000
transportation = 2500

# Processing: calculate total expenses
total_expenses = (
    rent
    + groceries
    + electricity
    + internet
    + transportation
)

# Processing: calculate remaining balance
remaining_balance = income - total_expenses

# Output: display the results
print("Monthly Income:", income)
print("Total Expenses:", total_expenses)
print("Remaining Balance:", remaining_balance)

"""
Expected Output

Monthly Income: 50000
Total Expenses: 26300
Remaining Balance: 23700
"""