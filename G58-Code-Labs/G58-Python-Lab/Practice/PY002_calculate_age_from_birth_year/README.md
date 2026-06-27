# PY002 — Calculate Age from Birth Year

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

A person's birth year is already stored in a variable.

Calculate their age assuming the current year is **2026**, and print the result.

---

## 2. Example

### Input (Starter Code)

```python
birth_year = 2005
```

### Output

```text
Age: 21
```

---

## 3. Constraints

- Use the given `birth_year` variable.
- Store the current year in a separate variable.
- Calculate the age using subtraction.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What information is already available?
- What needs to be calculated?
- Which mathematical operation should be used?
- Where should the result be stored?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Store the current year in a variable.

---

### Hint 2
Subtract birth year from current year.

---

### Hint 3
Store the result in a variable named `age`.

</details>

---

## 6. Learning Objectives

### Python
- Variables with numeric values
- Subtraction operator (`-`)
- `print()` function

### Programming
- Basic arithmetic operations
- Store → Process → Output flow
- Reusing existing data

---

## 7. Pattern Recognition

```
Store Data → Calculate → Output Result
```

This is one of the most common programming patterns in interviews.

---

## 8. Core Logic

The birth year is already given.

We store the current year in a variable, subtract birth year from it, and print the result as age.

---

## 9. Algorithm

1. Store birth year
2. Store current year (2026)
3. Subtract birth year from current year
4. Store result in `age`
5. Print age

---

## 10. Complexity

### Time Complexity

**O(1)**  
The program performs a fixed number of operations.

### Space Complexity

**O(1)**  
Only a few integer variables are used regardless of input size.

---

## 11. Pseudocode

```text
START

Store birth year

Store current year

age = current year - birth year

Print age

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Variable | Stores a value for reuse |
| Integer | Whole number like 10, 2026 |
| Assignment (`=`) | Stores value in variable |
| Subtraction (`-`) | Finds difference between numbers |
| Expression | A calculation that produces a value |

---

## 13. After Solving

- Work with numeric variables
- Perform subtraction
- Store computed results
- Print final output

---

## 14. Interview Follow-up Questions

**1. Why is the time complexity O(1)?**  
Because the program always performs a fixed number of operations regardless of input size.

---

**2. Why do we store the current year in a variable?**  
To make the program flexible and readable instead of hardcoding the expression everywhere.

---

**3. What happens if birth year is greater than current year?**  
The result becomes negative, which is logically invalid and should be validated in real applications.

---

**4. Can we directly print the result without storing it?**  
Yes, but storing it improves readability and debugging.

---

**5. Why is subtraction used here?**  
Because age is calculated as the difference between two years.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>