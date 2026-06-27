# PY009 — Split Restaurant Bill

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

Four friends went to a restaurant and decided to split the bill equally.

Calculate:

- Amount each person should pay

Use the values already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
Total Bill = 2400  
Number of People = 4
```

### Output

```text
Total Bill: 2400  
Number of People: 4  
Amount Per Person: 600.0
```

---

## 3. Constraints

- Use only the given values.
- Use division operator `/` for calculation.
- Store result in a variable.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What is being shared?
- How do we divide something equally?
- Which operator is used for division?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Use the division operator `/`.

---

### Hint 2
Formula:

```text
Amount Per Person = Total Bill / Number of People
```

---

### Hint 3
Store result before printing.

</details>

---

## 6. Learning Objectives

### Python
- Division operator `/`
- Variables
- Arithmetic expressions
- Floating-point results

### Programming
- Equal distribution logic
- Sharing values equally
- Input → Process → Output flow

---

## 7. Pattern Recognition

```
Total Value → Division → Equal Distribution
```

This pattern is widely used in financial and sharing systems.

---

## 8. Core Logic

The total bill is divided equally among all people using the division operator.

---

## 9. Algorithm

1. Store total bill
2. Store number of people
3. Divide bill by number of people
4. Store result
5. Print all values

---

## 10. Complexity

### Time Complexity

**O(1)**  
Fixed number of operations.

### Space Complexity

**O(1)**  
Uses only a constant number of variables.

---

## 11. Pseudocode

```text
START

Store total bill
Store number of people

amount_per_person = total_bill / number_of_people

Print total bill
Print number of people
Print amount per person

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Variable | Stores a value |
| Division (`/`) | Splits value into equal parts |
| Expression | A calculation |
| Operator | Symbol like `/` |
| Floating value | Decimal result |

---

## 13. After Solving

- Work with division
- Handle equal distribution
- Store computed results
- Print formatted output

---

## 14. Interview Follow-up Questions

**1. Why does division give a float result in Python?**  
Because `/` always returns a floating-point number for precision.

---

**2. What happens if number of people is 0?**  
It causes a division by zero error.

---

**3. Why do we store the result in a variable?**  
To reuse and clearly display computed values.

---

**4. What is the time complexity and why?**  
O(1), because only fixed arithmetic operations are performed.

---

**5. Can we write this in one line?**  
Yes:

```python
print("Amount Per Person:", 2400 / 4)
```

But structured code improves readability.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>