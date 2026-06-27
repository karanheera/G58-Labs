# Store the monthly income.
income = 50000

# Store each monthly expense.
rent = 15000
groceries = 6000
electricity = 1800
internet = 1000
transportation = 2500

# Add all expenses to find the total amount spent.
total_expenses = (
    rent
    + groceries
    + electricity
    + internet
    + transportation
)

# Calculate the money remaining after all expenses.
remaining_balance = income - total_expenses

# Display the final results.
print("Monthly Income:", income)
print("Total Expenses:", total_expenses)
print("Remaining Balance:", remaining_balance)

"""
Expected Output

Monthly Income: 50000
Total Expenses: 26300
Remaining Balance: 23700
"""