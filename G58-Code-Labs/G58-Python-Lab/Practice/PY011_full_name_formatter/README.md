# PY011 — Full Name Formatter

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

A registration system stores a person's first name and last name separately.

Combine them to display the person's full name.

Use the values already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
First Name = John  
Last Name = Smith
```

### Output

```text
First Name: John  
Last Name: Smith  

Full Name: John Smith
```

---

## 3. Constraints

- Use only the given values.
- Store names in variables.
- Use string concatenation.
- Do not use `input()`, loops, or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What text values are given?
- How do we join two strings?
- Where should the final result be stored?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Strings can be joined using `+`.

---

### Hint 2
Add a space between names:

```text
"John" + " " + "Smith"
```

---

### Hint 3
Store the final result in a new variable.

</details>

---

## 6. Learning Objectives

### Python
- String variables
- String concatenation
- Printing text output

### Programming
- Working with textual data
- Combining values
- Data formatting

---

## 7. Pattern Recognition

```
Text Part 1 + Separator + Text Part 2 → Final String
```

This pattern is widely used in formatting systems.

---

## 8. Core Logic

The first name and last name are combined using string concatenation with a space in between.

---

## 9. Algorithm

1. Store first name
2. Store last name
3. Concatenate both with a space
4. Store full name
5. Print all values

---

## 10. Complexity

### Time Complexity

**O(1)**  
String concatenation is constant time for fixed input size.

### Space Complexity

**O(1)**  
Stores a fixed number of string variables.

---

## 11. Pseudocode

```text
START

Store first name
Store last name

full_name = first_name + " " + last_name

Print first name
Print last name
Print full name

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| string | Text data |
| variable | Stores a value |
| concatenation | Joining strings |
| space | Separator between words |
| assignment | Storing a value |

---

## 13. After Solving

- Work with string values
- Combine multiple text fields
- Format output properly
- Understand concatenation

---

## 14. Interview Follow-up Questions

**1. Why do we need `" "` between names?**  
To ensure proper spacing between words.

---

**2. What happens if we don’t add space?**  
The output becomes `JohnSmith`, which is incorrect formatting.

---

**3. Is string concatenation expensive?**  
For small strings, it is O(1), but large repeated concatenations can become inefficient.

---

**4. Can we use another method instead of `+`?**  
Yes, `.join()` or f-strings can also be used.

---

**5. Which method is preferred in real systems?**  
f-strings are preferred for readability:

```python
full_name = f"{first_name} {last_name}"
```

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>