# PY006 — Monthly Expense Tracker

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 10 Minutes

---

### Problem

You are given a monthly income and several monthly expenses.

Calculate:

- Total Expenses
- Remaining Balance

Use the values already provided in the program.

---

### Example

### Input

```text
Monthly Income = 50000

Rent = 15000
Groceries = 6000
Electricity = 1800
Internet = 1000
Transportation = 2500
```

### Output

```text
Monthly Income: 50000
Total Expenses: 26300
Remaining Balance: 23700
```

---

### Constraints

- Use only the given values.
- Store each value in a separate variable.
- Do not use `input()`.
- Do not use loops or functions.

---

### Think Before You Code

Before writing any code, think about the following:

- Which values are expenses?
- How can all expenses be combined into one value?
- How is the remaining balance calculated?
- Which result should be calculated first?

Try solving the problem before viewing the hints.

---

<details>

<summary>Need a Hint?</summary>

### Hint 1

Store each amount in its own variable.

---

### Hint 2

Find the **Total Expenses** first.

---

### Hint 3

Use this formula:

```text
Remaining Balance = Monthly Income - Total Expenses
```

</details>

---

### Learning Objectives

By completing this exercise, you will learn how to:

### Python

- Store data using variables.
- Assign values using `=`.
- Display output using `print()`.

### Programming

- Break a problem into smaller steps.
- Perform arithmetic calculations.
- Store → Process → Display information.

---

### Pattern Recognition

This problem introduces one of the most common programming patterns:

```text
Store Data
      ↓
Process Data
      ↓
Display Result
```

You'll use this pattern throughout programming, whether you're building calculators, banking software, games, or web applications.

---

### Core Logic

The program already contains all the required information.

First, store each value in a variable.

Next, add every expense to calculate the total spending.

Finally, subtract the total expenses from the monthly income to find the remaining balance.

---

### Algorithm

1. Store the monthly income.
2. Store each expense.
3. Calculate the total expenses.
4. Calculate the remaining balance.
5. Display all results.

---

### Pseudocode

```text
START

Store monthly income

Store rent
Store groceries
Store electricity
Store internet
Store transportation

Total Expenses = Rent + Groceries + Electricity + Internet + Transportation

Remaining Balance = Monthly Income - Total Expenses

Display Monthly Income
Display Total Expenses
Display Remaining Balance

END
```

---

### Notes

| Term | Meaning |
|------|---------|
| Variable | Stores a value for later use. |
| Assignment (`=`) | Stores a value inside a variable. |
| Expression | A calculation that produces a value. |
| Arithmetic | Mathematical operations like `+` and `-`. |
| `print()` | Displays output on the screen. |

---

### After Solving, You Should Be Able To

- Create variables.
- Store numeric values.
- Perform addition and subtraction.
- Build simple mathematical expressions.
- Print meaningful results.
- Break a simple problem into logical steps.

---

### Interview Insight

This exercise tests your ability to:

- Understand problem requirements.
- Store values correctly.
- Perform basic arithmetic.
- Produce the required output.

**Interview Difficulty:** Easy

---

# Real-World Usage

This same logic is used in:

- Personal budgeting
- Expense tracking applications
- Banking software
- Accounting systems
- Business finance dashboards

---

<details>

<summary>Solution (Open Only After Trying)</summary>

[**solution.py**](solution.py)

</details>
