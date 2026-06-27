# PY012 — Email Username Extractor

**Difficulty:** ★★☆☆☆ Beginner  
**Estimated Time:** 7 Minutes

---

## 1. Problem

An email address contains two parts:

- Username
- Domain

Extract and display only the **username** from the email address.

Use the value already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
Email = john.smith@gmail.com
```

### Output

```text
Email: john.smith@gmail.com  

Username: john.smith
```

---

## 3. Constraints

- Use only the given email value.
- Extract username using string slicing.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What is the structure of an email?
- Where does the username end?
- How can we extract part of a string?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Email format:

```text
username@domain
```

---

### Hint 2
Find position of `@`.

---

### Hint 3
Use slicing:

```text
text[start:end]
```

</details>

---

## 6. Learning Objectives

### Python
- String slicing
- Index-based extraction
- String variables

### Programming
- Data extraction from structured text
- Working with substrings
- Understanding string structure

---

## 7. Pattern Recognition

```
Full String → Extract Substring → Required Part
```

This pattern is used in almost all parsing systems.

---

## 8. Core Logic

The username is the part of the email before the `@` symbol.

We extract it using string slicing.

---

## 9. Algorithm

1. Store email address
2. Find position of `@`
3. Slice string from start to `@`
4. Store username
5. Print results

---

## 10. Complexity

### Time Complexity

**O(n)**  
Where `n` is the length of the string (searching or slicing depends on string size).

---

### Space Complexity

**O(n)**  
Stores original email and extracted substring.

---

## 11. Pseudocode

```text
START

Store email address

Find position of "@"

username = email from start to "@"

Print email
Print username

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| string | Text data |
| slicing | Extracting part of a string |
| index | Position of a character |
| substring | Part of a string |
| delimiter | Character used to split data |
| variable | Stores a value |

---

## 13. After Solving

- Work with string slicing
- Extract structured data
- Understand string positions
- Handle text parsing

---

## 14. Interview Follow-up Questions

**1. Why do we slice up to `@`?**  
Because everything before `@` is the username in email format.

---

**2. What happens if `@` is missing?**  
The logic breaks; slicing becomes invalid for extraction.

---

**3. Is slicing O(1)?**  
No, slicing depends on string size → O(n).

---

**4. Why is string slicing useful?**  
It helps extract meaningful parts of structured text.

---

**5. Can this be done without slicing?**  
Yes, using `.split("@")[0]` which is more readable in real applications.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>