# PY002 - Calculate Age from Birth Year

## Problem Statement

***A person's birth year is already stored in a variable. Calculate their age assuming the current year is 2026, and print the result.***

### Starter Code

```python
birth_year = 2005
```

Complete the program to print the person's age.

---

### Example

**Code**

```python
birth_year = 2000
```

**Output**

```text
Age: 25
```

---

### ⚠️ Important Rule

Try solving it yourself before checking the solution.

## How to Think About the Problem

Before coding:

- What information is already available?
- What information do you need to calculate?
- Which mathematical operation will help?

Think on paper, MS Word, or a notebook before writing code.

---

<details>

<summary>Approach</summary>

- Store the current year in a variable.
- Subtract the birth year from the current year.
- Store the result in another variable.
- Print the age.

</details>

---

<details>

<summary>Algorithm</summary>

1. Store the birth year.
2. Store the current year (2026).
3. Calculate age using subtraction.
4. Print the result.

</details>

---

<details>

<summary>Pseudocode</summary>

```
START

SET birth_year = given value
SET current_year = 2026

age = current_year - birth_year

PRINT age

END
```

</details>

---

<details>

<summary>Complexity</summary>

### Time Complexity

The program performs one subtraction and one print operation.

**Overall Time Complexity: `O(1)`**

(Constant time)

### Space Complexity

The program stores only a few integer variables.

**Overall Space Complexity: `O(1)`**

(Constant space)

</details>

---

<details>

<summary>Glossary (Technical Terms)</summary>

| Term | Meaning |
|------|------------------|
| Variable | A named container that stores a value. |
| Integer | A whole number like 10, 50, or 2025. |
| Assignment (`=`) | Putting a value into a variable. |
| Arithmetic | Doing maths like addition, subtraction, multiplication, or division. |
| Subtraction (`-`) | Finding the difference between two numbers. |
| Expression | A calculation that produces a value, such as `2026 - birth_year`. |
| Output | The information shown on the screen. |

</details>

---

<details>

<summary>Key Learning</summary>

- Variables
- Integer values
- Arithmetic operations
- Subtraction
- Storing calculated values
- Printing output

</details>

---

<details>

<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

</details>

---

## Real-World Use Case

Age calculations are commonly used in:

- School admission systems
- Online registration forms
- Hospital management software
- Banking applications
- Insurance systems
- Government portals