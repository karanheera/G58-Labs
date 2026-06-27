# PY005 — Simple Interest Calculator

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

Given principal, rate, and time, calculate simple interest and display the result.

---

## 2. Example

### Input

```text
P = 1000  
R = 5  
T = 2
```

### Output

```text
Simple Interest: 100.0
```

---

## 3. Constraints

- Use given values of P, R, and T.
- Apply the correct formula.
- Store the result in a variable.
- Print output exactly as shown.
- Do not use loops or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What values are already given?
- What formula connects them?
- What operations are required?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Use the formula:

```text
SI = (P × R × T) / 100
```

---

### Hint 2
Multiply first, then divide by 100.

---

### Hint 3
Store the result before printing.

</details>

---

## 6. Learning Objectives

### Python
- Multiple variables
- Arithmetic expressions
- Order of operations
- Mathematical formulas

### Programming
- Combine multiple inputs
- Apply formulas
- Store computed results
- Input → Process → Output flow

---

## 7. Pattern Recognition

```
Multiple Inputs → Formula → Output
```

This pattern is widely used in financial and calculation-based programs.

---

## 8. Core Logic

The program takes three values: principal, rate, and time.

It applies the simple interest formula and prints the calculated result.

---

## 9. Algorithm

1. Store principal (P), rate (R), and time (T)
2. Apply formula (P × R × T) / 100
3. Store result in variable
4. Print result

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

Store P, R, T

SI = (P * R * T) / 100

Print SI

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Principal | Initial amount of money |
| Rate | Percentage of interest |
| Time | Duration in years |
| Formula | Mathematical rule |
| Expression | Calculation using operators |

---

## 13. After Solving

- Work with multiple variables
- Apply formulas correctly
- Perform chained arithmetic operations
- Print computed results

---

## 14. Interview Follow-up Questions

**1. Why do we multiply P, R, and T first?**  
Because multiplication has higher precedence than division in arithmetic expressions.

---

**2. Why do we divide by 100?**  
Because the rate is given in percentage form.

---

**3. What is the time complexity and why?**  
It is O(1) because the number of operations does not depend on input size.

---

**4. What happens if we change the order of operations?**  
Incorrect order may produce wrong results due to operator precedence rules.

---

**5. Can this be written in one line?**  
Yes:

```python
print("Simple Interest:", (1000 * 5 * 2) / 100)
```

But using variables improves readability and maintainability.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>