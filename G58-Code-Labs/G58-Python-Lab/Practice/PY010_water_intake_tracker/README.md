# PY010 — Water Intake Tracker

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 8 Minutes

---

## 1. Problem

A health app tracks how much water a person drinks in a day.

Calculate:

- Total water consumed
- Remaining water needed to reach the daily goal

Use the values already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
Daily Goal = 3000 ml

Morning = 750 ml  
Afternoon = 1000 ml  
Evening = 500 ml
```

### Output

```text
Daily Goal: 3000 ml  
Total Water Consumed: 2250 ml  
Remaining Water Needed: 750 ml
```

---

## 3. Constraints

- Use only the given values.
- Store each value in a separate variable.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What values contribute to total water intake?
- Which operation combines these values?
- How do we compare total with the goal?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Add all water values together.

---

### Hint 2
Use subtraction for remaining water.

---

### Hint 3
Formula:

```text
Remaining = Goal - Total
```

</details>

---

## 6. Learning Objectives

### Python
- Multiple variable addition
- Subtraction
- Arithmetic expressions
- Sequential calculations

### Programming
- Step-by-step problem solving
- Multi-stage calculations
- Store → Process → Output flow

---

## 7. Pattern Recognition

```
Multiple Inputs → Sum → Compare → Result
```

This pattern is common in tracking systems.

---

## 8. Core Logic

First calculate total water intake by adding all sessions.

Then subtract it from the daily goal to find remaining water needed.

---

## 9. Algorithm

1. Store daily water goal
2. Store morning, afternoon, evening intake
3. Add all values to get total
4. Subtract total from goal
5. Display results

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

Store daily goal

Store morning intake
Store afternoon intake
Store evening intake

total = morning + afternoon + evening

remaining = goal - total

Print goal
Print total
Print remaining

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Variable | Stores a value |
| Addition | Combining values |
| Subtraction | Finding difference |
| Total | Sum of values |
| Goal | Target value |
| Expression | A calculation |

---

## 13. After Solving

- Combine multiple inputs
- Perform chained calculations
- Compare values
- Store intermediate results

---

## 14. Interview Follow-up Questions

**1. Why do we calculate total first?**  
Because remaining depends on total consumption.

---

**2. What happens if one value is missing?**  
The total and remaining values will be incorrect.

---

**3. Why is this O(1) complexity?**  
Because operations are fixed and do not depend on input size.

---

**4. Why store values separately instead of directly adding?**  
It improves readability and debugging.

---

**5. Can this be written in one line?**  
Yes:

```python
print("Remaining:", 3000 - (750 + 1000 + 500))
```

But step-by-step code is easier to maintain.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>