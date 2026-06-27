# PY013 — Phone Number Cleaner

**Difficulty:** ★★☆☆☆ Beginner  
**Estimated Time:** 7 Minutes

---

## 1. Problem

A phone number is stored in a messy format with special characters.

Clean the phone number so that only digits remain.

Use the value already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
Phone Number = "9876-543-210"
```

### Output

```text
Original Phone Number: 9876-543-210  

Cleaned Phone Number: 9876543210
```

---

## 3. Constraints

- Use only the given phone number.
- Remove unwanted characters using string methods.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What characters are not needed?
- What should the final output look like?
- How can we remove unwanted symbols?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Use `replace()` method.

---

### Hint 2
Replace `"-"` with an empty string `""`.

---

### Hint 3
Apply multiple `replace()` calls if needed.

</details>

---

## 6. Learning Objectives

### Python
- String methods
- `replace()` function
- String manipulation
- Data transformation

### Programming
- Data cleaning
- Text normalization
- Input sanitization logic

---

## 7. Pattern Recognition

```
Raw Data → Clean → Structured Data
```

This pattern is essential in all real-world systems.

---

## 8. Core Logic

Remove unwanted characters from a string using string replacement methods to produce a clean numeric format.

---

## 9. Algorithm

1. Store phone number
2. Replace `-` with empty string
3. Store cleaned number
4. Print original number
5. Print cleaned number

---

## 10. Complexity

### Time Complexity

**O(n)**  
Where `n` is the length of the string (each replace scans the string).

---

### Space Complexity

**O(n)**  
Stores original and cleaned string.

---

## 11. Pseudocode

```text
START

Store phone number

Clean phone number using replace()

Store cleaned number

Display original number

Display cleaned number

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| string | Text data |
| replace() | Replaces part of a string |
| cleaning | Removing unwanted characters |
| delimiter | Symbol used to separate data |
| transformation | Converting data format |

---

## 13. After Solving

- Clean messy data
- Use string methods
- Transform raw input into usable format
- Understand basic data preprocessing

---

## 14. Interview Follow-up Questions

**1. Why do we use `replace()` instead of slicing?**  
Because `replace()` removes specific characters regardless of position.

---

**2. What happens if multiple unwanted characters exist?**  
We can chain `replace()` calls or extend logic.

---

**3. Is `replace()` in-place?**  
No, it returns a new string.

---

**4. Why is this operation O(n)?**  
Because the string must be scanned to find characters to replace.

---

**5. Can we use regex instead?**  
Yes, `re.sub()` is used in advanced cleaning scenarios.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>