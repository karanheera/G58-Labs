# PY008 — Salary After Tax

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 10 Minutes

---

## 1. Problem

A company needs to calculate an employee's salary after deducting income tax.

Calculate:

- Tax amount
- Salary after tax

Use the values already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
Monthly Salary = 60000  
Tax Rate = 10%
```

### Output

```text
Monthly Salary: 60000  
Tax Amount: 6000.0  
Salary After Tax: 54000.0
```

---

## 3. Constraints

- Use only the given values.
- Convert percentage into decimal form.
- Store all results in variables.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- How do we convert percentage into a usable number?
- What is the first value to calculate?
- How is final salary derived?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Convert percentage:

```text
10% = 10 / 100 = 0.1
```

---

### Hint 2
Multiply salary by tax rate.

---

### Hint 3
Subtract tax from salary.

</details>

---

## 6. Learning Objectives

### Python
- Percentage calculations
- Variables
- Multiplication and subtraction
- Floating-point numbers

### Programming
- Financial calculations
- Derived values from base data
- Store → Process → Output flow

---

## 7. Pattern Recognition

```
Base Value → Percentage Calculation → Final Result
```

This pattern is heavily used in financial systems.

---

## 8. Core Logic

The salary is given.

We calculate tax using percentage, then subtract it from salary to get final take-home pay.

---

## 9. Algorithm

1. Store salary
2. Store tax rate
3. Convert percentage to decimal
4. Calculate tax amount
5. Subtract tax from salary
6. Print results

---

## 10. Complexity

### Time Complexity

**O(1)**  
Fixed number of arithmetic operations.

### Space Complexity

**O(1)**  
Uses only a constant number of variables.

---

## 11. Pseudocode

```text
START

Store salary
Store tax rate

tax = salary × (tax_rate / 100)

salary_after_tax = salary - tax

Print salary
Print tax
Print salary_after_tax

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Variable | Stores data |
| Percentage | Value out of 100 |
| Decimal | Converted percentage form |
| Multiplication | Used to calculate percentage |
| Subtraction | Used to get final value |

---

## 13. After Solving

- Work with percentages
- Convert values correctly
- Perform chained calculations
- Store intermediate results

---

## 14. Interview Follow-up Questions

**1. Why do we divide percentage by 100?**  
Because percentages are based on a scale of 100.

---

**2. Why do we multiply salary with tax rate?**  
To find the portion of salary that should be deducted.

---

**3. Why is the time complexity O(1)?**  
Because operations do not depend on input size.

---

**4. What happens if we forget to convert percentage?**  
The tax amount will be 100 times larger than expected.

---

**5. Can this be written in one line?**  
Yes:

```python
print("Salary After Tax:", 60000 - (60000 * 0.1))
```

But splitting improves readability and debugging.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>