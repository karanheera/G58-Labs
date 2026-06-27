# PY006 — Monthly Expense Tracker

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 10 Minutes

---

## 1. Problem

You are given a monthly income and several monthly expenses.

Calculate:

- Total Expenses
- Remaining Balance

Use the values already provided in the program.

---

## 2. Example

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

## 3. Constraints

- Use only the given values.
- Store each value in a separate variable.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What values are expenses?
- How can all expenses be combined?
- What should be calculated first?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Store each expense in a separate variable.

---

### Hint 2
Add all expenses first.

---

### Hint 3
Use:

```text
Remaining Balance = Income - Total Expenses
```

</details>

---

## 6. Learning Objectives

### Python
- Variable assignment
- Arithmetic operations (`+`, `-`)
- `print()` function

### Programming
- Break problem into steps
- Store → Process → Output pattern
- Working with multiple variables

---

## 7. Pattern Recognition

```
Store Data → Process Data → Display Result
```

This pattern is used in almost all real-world applications.

---

## 8. Core Logic

Store all income and expense values in variables, sum all expenses, then subtract from income to get remaining balance.

---

## 9. Algorithm

1. Store monthly income
2. Store all expenses
3. Add all expenses
4. Subtract from income
5. Print results

---

## 10. Complexity

### Time Complexity

**O(1)**  
Fixed number of arithmetic operations.

### Space Complexity

**O(1)**  
Uses only a fixed number of variables.

---

## 11. Pseudocode

```text
START

Store income

Store rent
Store groceries
Store electricity
Store internet
Store transportation

total_expenses = sum of all expenses

remaining_balance = income - total_expenses

Print income
Print total expenses
Print remaining balance

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Variable | Stores a value |
| Assignment (`=`) | Assigns value to variable |
| Expression | A calculation |
| Arithmetic | Mathematical operations |
| `print()` | Displays output |

---

## 13. After Solving

- Work with multiple variables
- Perform summation
- Apply subtraction logic
- Format output correctly

---

## 14. Interview Follow-up Questions

**1. Why do we calculate total expenses first?**  
Because remaining balance depends on total expenses.

---

**2. Why use separate variables for each expense?**  
It improves readability and makes debugging easier.

---

**3. What is the time complexity and why?**  
O(1), because operations are fixed regardless of input size.

---

**4. What happens if we miss one expense?**  
The total expense and final balance will be incorrect.

---

**5. Can we use a single line for total expenses?**  
Yes:

```python
total = rent + groceries + electricity + internet + transportation
```

But separating improves clarity.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>