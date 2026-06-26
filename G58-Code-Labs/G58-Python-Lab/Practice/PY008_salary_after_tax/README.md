# PY008 - Salary After Tax

**Difficulty:** ★☆☆☆☆ Beginner


## Problem Statement

A company needs to calculate an employee's salary after deducting income tax.

Calculate:

- Tax amount
- Salary after tax

Use the values already provided in the program.

---

### Given Data

```
Monthly Salary = 60000
Tax Rate = 10%
```

---

### Formula

```
Tax Amount = Salary × Tax Rate

Salary After Tax = Salary − Tax Amount
```

---

### Expected Output

```
Monthly Salary: 60000
Tax Amount: 6000.0
Salary After Tax: 54000.0
```

---

## ⭐ Key Concept (Very Important)

This program introduces **percentage calculations**.

A percentage tells us what part of a value should be calculated.

In Python:

```python
tax_rate = 10 / 100
```

This converts **10%** into **0.10**, which can be used in calculations.

Example:

```python
tax = salary * tax_rate
```

---

## Why this matters

Percentage calculations are used every day in:

- Employee payroll
- Income tax
- Shopping discounts
- Bank interest
- Insurance premiums
- Investment returns

---

## How to Think About the Problem

Ask yourself:

- What is the employee's salary?
- What percentage should be deducted?
- How is the tax amount calculated?
- How do we find the remaining salary?

---

<details>

<summary>Approach</summary>

- Store the monthly salary
- Store the tax rate
- Calculate the tax amount
- Calculate the salary after tax
- Display the results

</details>

---

<details>

<summary>Algorithm</summary>

1. Store monthly salary
2. Store tax rate
3. Calculate tax amount
4. Calculate salary after tax
5. Display all values

</details>

---

<details>

<summary>Pseudocode</summary>

```
START

Store salary

Store tax rate

Calculate tax amount

Calculate salary after tax

Display salary

Display tax amount

Display salary after tax

END
```

</details>

---

<details>

<summary>Glossary</summary>

| Term | Meaning |
|------|---------|
| variable | Stores a value |
| percentage | A value out of 100 |
| expression | A mathematical calculation |
| multiplication | Finding a percentage of a value |
| subtraction | Taking one value away from another |
| tax | Money deducted from income |

</details>

---

<details>

<summary>Key Learning</summary>

- Variables
- Percentage calculations
- Multiplication
- Subtraction
- Storing calculated values
- Displaying results

</details>

---

<details>

<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

</details>

---

## Real-World Use Case

Salary calculations are used in:

- Payroll software
- Human Resources (HR) systems
- Accounting applications
- Banking systems
- Government tax portals