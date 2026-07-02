# PY015 — Character Counter

**Difficulty:** ★★☆☆☆ Beginner  
**Estimated Time:** 7 Minutes

---

## 1. Problem

Given a word or sentence, count how many characters it contains.

Store the text inside a variable and display:

- Original text
- Total number of characters

Use the value already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
Text = Python Programming
```

### Output

```text
Text: Python Programming

Total Characters: 18
```

---

## 3. Constraints

- Use only the given text value.
- Do not use `input()`.
- Do not use loops.
- Do not count characters manually.
- Use Python's built-in functionality.

---

## 4. Think Before You Code

Before writing any code, think about:

- What is a character?
- Do spaces count as characters?
- Is there a Python feature that already knows the length of a string?
- How can we store the count for later use?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1

Every letter, digit, symbol, and space is considered a character.

Example:

```text
Hello World
```

contains 11 characters because the space is also counted.

---

### Hint 2

Python provides a built-in function that returns the length of an object.

---

### Hint 3

The function name is:

```python
len()
```

</details>

---

## 6. Learning Objectives

### Python

- Strings
- Variables
- Built-in functions
- `len()` function
- Printing formatted output

### Programming

- Counting data
- Measuring data size
- Understanding string length
- Using built-in utilities

---

## 7. Pattern Recognition

```
Store Text
      ↓
Measure Length
      ↓
Store Result
      ↓
Display Output
```

Many real-world programs first measure data before processing it further.

Examples include:

- Password validation
- Username length checking
- Tweet character limits
- File name validation
- Data preprocessing

---

## 8. Core Logic

Python already knows how many characters exist inside a string.

The `len()` function calculates the total number of characters, including:

- Letters
- Numbers
- Spaces
- Symbols
- Punctuation

There is no need to count them manually.

---

## 9. Algorithm

1. Store the text.
2. Calculate its length using `len()`.
3. Store the result.
4. Print the original text.
5. Print the total number of characters.

---

## 10. Complexity

### Time Complexity

**O(n)**

Where **n** is the number of characters in the string.

### Why?

Although using `len(text)` looks like a single operation, thinking from an algorithmic perspective, determining the total size of data conceptually depends on the number of characters being measured.

In CPython (the standard Python implementation), `len()` for strings is stored internally and is effectively **O(1)** because Python remembers the length of the string.

However, beginners should understand the general algorithmic idea that counting characters normally requires looking at all characters once, which would be **O(n)** in many programming situations or custom implementations.

This distinction is useful during interviews.

---

### Space Complexity

**O(1)**

### Why?

Only one additional integer variable (`character_count`) is created.

The amount of extra memory does not increase with the size of the string.

---

## 11. Pseudocode

```text
START

Store text

character_count = length of text

Print text

Print character_count

END
```

---

## 12. Notes

| Term | Meaning |
|------|---------|
| character | A single letter, number, symbol, or space |
| string | A sequence (collection) of characters |
| length | Total number of characters |
| built-in function | A function already provided by Python |
| variable | A named storage location for data |
| return value | The result produced by a function |
| constant time (O(1)) | Execution time stays nearly the same regardless of input size |
| linear time (O(n)) | Execution time grows with the amount of data |

---

## 13. Python Documentation

### `len()`

Official Python Documentation:

https://docs.python.org/3/library/functions.html#len

The `len()` function returns the number of items inside an object.

For strings, it returns the total number of characters.

Example:

```python
text = "Python"

print(len(text))
```

Output

```text
6
```

---

## 14. After Solving

You should now understand how to:

- Count characters in a string
- Use Python's `len()` function
- Store calculated values
- Print multiple variables
- Measure text size
- Recognize when built-in functions simplify programming

---

## 15. Interview Follow-up Questions

### 1. What does `len()` return?

It returns the total number of items inside an object.

For strings, it returns the number of characters.

---

### 2. Does `len()` count spaces?

Yes.

Spaces are valid characters.

---

### 3. Does `len()` count punctuation?

Yes.

Symbols such as `!`, `.`, `@`, and `#` are also characters.

---

### 4. What is the return type of `len()`?

It returns an integer (`int`).

---

### 5. Why is `len()` considered a built-in function?

Because Python already provides it without requiring additional libraries.

---

### 6. Can `len()` work only with strings?

No.

It also works with lists, tuples, dictionaries, sets, bytes, and many other collections.

---

### 7. What happens if we call `len("")`?

It returns:

```text
0
```

because the string contains no characters.

---

### 8. Why don't we manually count characters?

Manual counting is slow, error-prone, and unnecessary because Python already provides an optimized solution.

---

### 9. Why is the space complexity O(1)?

Only one extra integer variable is stored regardless of how long the text becomes.

---

### 10. In CPython, why is `len()` often considered O(1)?

Because Python stores the length of strings internally, allowing it to return the value immediately without traversing the string.

This is a common interview discussion point.

---

## 16. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[**solution.py**](solution.py)

</details>