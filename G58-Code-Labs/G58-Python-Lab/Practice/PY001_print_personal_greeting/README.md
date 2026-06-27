# PY001 — Print Personal Greeting

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

Write a program that reads a user's name and prints a greeting message.

---

## 2. Example

### Input

```text
John
```

### Output

```text
Hello, John
```

---

## 3. Constraints

- Use `input()` to read the user's name.
- Store the input in a variable.
- Print the greeting exactly as shown.
- Do not use loops or functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What information is being given?
- Where will the input be stored?
- How will the output use that input?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1
Use `input()` to read user input.

---

### Hint 2
Store it in a variable.

---

### Hint 3
Print `"Hello, "` + name.

</details>

---

## 6. Learning Objectives

### Python
- `input()` function
- variables
- `print()` function

### Programming
- input → process → output flow
- data storage and reuse

---

## 7. Pattern Recognition

```
Input → Store → Output
```

---

## 8. Core Logic

Take input from the user, store it in a variable, and print a greeting using that variable.

---

## 9. Algorithm

1. Read input from user
2. Store it in a variable
3. Print greeting message

---

## 10. Complexity

### Time Complexity

**O(n)**  
Depends on length of input string.

### Space Complexity

**O(n)**  
Stores input string in memory.

---

## 11. Pseudocode

```text
START

READ name

PRINT "Hello, " + name

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| `input()` | Reads user input as a string |
| Variable | Stores data for reuse |
| `=` | Assigns value to a variable |
| `print()` | Displays output |
| String | Sequence of characters (text) |

---

## 13. After Solving

- Read user input
- Store values in variables
- Print formatted output
- Understand input → output flow

---

## 14. Interview Follow-up Questions

**1. What does `input()` return?**  
It always returns a string, even if the input looks like a number.

---

**2. Why do we store input in a variable?**  
So we can reuse the value later without asking the user again.

---

**3. What happens if we don't use a variable?**  
We can still print directly, but the code becomes less readable and harder to extend.

---

**4. What happens if the user enters nothing?**  
An empty string is returned, and the program prints only `"Hello, "`.

---

**5. Can this problem be solved in one line?**  
Yes:

```python
print("Hello,", input())
```

But using variables improves clarity and maintainability.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>


[**solution.py**](solution.py)

</details>