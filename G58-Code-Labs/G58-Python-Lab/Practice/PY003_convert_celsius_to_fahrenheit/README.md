# PY003 — Convert Celsius to Fahrenheit

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

The temperature in Celsius is already stored in a variable.

Convert it to Fahrenheit and print the result.

---

## 2. Example

### Input (Starter Code)

```python
celsius = 40
```

### Output

```text
Fahrenheit: 104.0
```

---

## 3. Constraints

- Use the given `celsius` variable.
- Apply the correct conversion formula.
- Store the result in a variable.
- Print the output exactly as shown.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What value is already given?
- What formula is needed for conversion?
- Where should the result be stored?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Use the formula:

```text
(F = (C × 9/5) + 32)
```

---

### Hint 2
Multiply first, then divide, then add 32.

---

### Hint 3
Store the result in a variable before printing.

</details>

---

## 6. Learning Objectives

### Python
- Variables with float values
- Arithmetic expressions
- Mathematical formulas
- `print()` function

### Programming
- Apply formulas to data
- Store computed results
- Input → Process → Output flow

---

## 7. Pattern Recognition

```
Store Data → Apply Formula → Output Result
```

This pattern is widely used in calculation-based programs.

---

## 8. Core Logic

The Celsius temperature is already provided.

We apply the conversion formula `(C × 9/5) + 32`, store the result, and print the Fahrenheit value.

---

## 9. Algorithm

1. Read Celsius value
2. Apply conversion formula
3. Store result in variable
4. Print Fahrenheit value

---

## 10. Complexity

### Time Complexity

**O(1)**  
The program performs a fixed number of arithmetic operations.

### Space Complexity

**O(1)**  
Only a few variables are used regardless of input size.

---

## 11. Pseudocode

```text
START

Store Celsius value

fahrenheit = (celsius × 9 / 5) + 32

Print fahrenheit

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Variable | Stores a value for reuse |
| Float | Number with decimals |
| Expression | A mathematical calculation |
| Formula | Rule used to compute values |
| Arithmetic | Mathematical operations |

---

## 13. After Solving

- Work with mathematical formulas
- Use arithmetic expressions
- Store computed values
- Print formatted output

---

## 14. Interview Follow-up Questions

**1. Why is this formula used?**  
Because Celsius and Fahrenheit are two different temperature scales with a fixed conversion relationship.

---

**2. Why do we use parentheses in the formula?**  
To ensure multiplication and division happen before addition, following mathematical precedence.

---

**3. Why is the time complexity O(1)?**  
Because the number of operations does not change with input size.

---

**4. What is the difference between int and float here?**  
The result may include decimals, so float is used instead of integer.

---

**5. Can we write this in one line?**  
Yes:

```python
print("Fahrenheit:", (celsius * 9 / 5) + 32)
```

But storing the value improves readability and debugging.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>