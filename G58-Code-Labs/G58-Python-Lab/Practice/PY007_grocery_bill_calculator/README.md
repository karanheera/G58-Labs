# PY007 — Grocery Bill Calculator

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 10 Minutes

---

## 1. Problem

A grocery store has the following items in a shopping basket.

Calculate:

- Total grocery bill

Use the values already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
Rice = 850  
Milk = 120  
Bread = 45  
Eggs = 180  
Fruits = 325
```

### Output

```text
Rice: 850  
Milk: 120  
Bread: 45  
Eggs: 180  
Fruits: 325  

Total Grocery Bill: 1520
```

---

## 3. Constraints

- Use only the given values.
- Store each item price in a separate variable.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What values are already given?
- What needs to be calculated?
- How will the total be computed?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Store each item price in a variable.

---

### Hint 2
Add all variables together.

---

### Hint 3
Store the result in a `total` variable.

</details>

---

## 6. Learning Objectives

### Python
- Variables
- Arithmetic addition
- Storing computed values
- `print()` function

### Programming
- Summing multiple values
- Store → Process → Output pattern
- Working with grouped data

---

## 7. Pattern Recognition

```
Multiple Values → Addition → Total Result
```

This pattern is used in billing and calculation systems.

---

## 8. Core Logic

Each grocery item price is stored in a variable.

All values are added together to calculate the total bill.

---

## 9. Algorithm

1. Store prices of all grocery items
2. Add all values
3. Store result in `total`
4. Print each item
5. Print total bill

---

## 10. Complexity

### Time Complexity

**O(1)**  
Fixed number of arithmetic operations.

### Space Complexity

**O(1)**  
Uses a constant number of variables.

---

## 11. Pseudocode

```text
START

Store rice price
Store milk price
Store bread price
Store eggs price
Store fruits price

total = sum of all items

Print all items
Print total bill

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
| Total | Sum of values |

---

## 13. After Solving

- Work with multiple variables
- Perform addition operations
- Store computed totals
- Print structured output

---

## 14. Interview Follow-up Questions

**1. Why do we store each item separately?**  
To keep data organized and easy to manage.

---

**2. Why do we calculate total at the end?**  
Because it depends on all individual item values.

---

**3. What is the time complexity and why?**  
O(1), because operations are fixed regardless of input size.

---

**4. What happens if one item is missing?**  
The total bill will be incorrect.

---

**5. Can we calculate total in one line?**  
Yes:

```python
total = rice + milk + bread + eggs + fruits
```

But separating improves readability and debugging.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>