# PY004 — Convert Kilometers to Miles

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

A distance in kilometers is given by the user.

Convert it into miles and display the result.

---

## 2. Example

### Input

```text
10
```

### Output

```text
Miles: 6.21371
```

---

## 3. Constraints

- Take input from the user.
- Convert input into a number using `float()`.
- Use the conversion formula correctly.
- Print the result exactly as shown.
- Do not use loops or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What type is the input coming as?
- What type is needed for calculation?
- What formula converts kilometers to miles?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
`input()` returns a string.

---

### Hint 2
Convert input using `float(input())`.

---

### Hint 3
Multiply by `0.621371`.

</details>

---

## 6. Learning Objectives

### Python
- `input()` function
- `float()` type conversion
- arithmetic operations
- constants in expressions

### Programming
- handling user input
- type conversion
- input → process → output flow

---

## 7. Pattern Recognition

```
Input (string) → Convert type → Calculate → Output
```

This is a very common real-world programming pattern.

---

## 8. Core Logic

The program takes distance in kilometers as input (string), converts it into a float, applies the conversion formula, and prints the result in miles.

---

## 9. Algorithm

1. Read input from user
2. Convert input to float
3. Multiply by 0.621371
4. Store result
5. Print result

---

## 10. Complexity

### Time Complexity

**O(1)**  
The program performs a fixed number of operations.

### Space Complexity

**O(1)**  
Only a few variables are used regardless of input size.

---

## 11. Pseudocode

```text
START

READ km as string
CONVERT km to float

miles = km * 0.621371

PRINT miles

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| `input()` | Reads data as string |
| `float()` | Converts string to decimal number |
| Type conversion | Changing data type |
| Constant | Fixed value like 0.621371 |
| Expression | A mathematical calculation |

---

## 13. After Solving

- Take user input
- Convert string to number
- Perform multiplication
- Print formatted output

---

## 14. Interview Follow-up Questions

**1. Why do we use `float(input())` instead of just `input()`?**  
Because `input()` returns a string, and mathematical operations require numeric types.

---

**2. What happens if we don’t convert input to float?**  
The program will throw a TypeError when trying to multiply a string with a float.

---

**3. Why is type conversion important in programming?**  
Because real-world input is often text, but calculations require numbers.

---

**4. Why is the time complexity O(1)?**  
Because the program performs a fixed number of operations regardless of input.

---

**5. Can we write this in one line?**  
Yes:

```python
print("Miles:", float(input()) * 0.621371)
```

But separating steps improves readability and debugging.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>