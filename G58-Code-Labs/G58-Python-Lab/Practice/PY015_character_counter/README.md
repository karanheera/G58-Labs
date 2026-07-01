# PY015 — Character Counter

**Difficulty:** ★★☆☆☆ Beginner  
**Estimated Time:** 8 Minutes

---

## 1. Problem

Given a string, display each visible character along with its index.

The output should be displayed in two horizontal lines:

- First line → Index values
- Second line → Corresponding characters

Whitespace characters should **not** be counted or displayed.

---

## 2. Example

### Given Data

```text
P y t h o n
```

### Output

```text
0 1 2 3 4 5
P y t h o n
```

---

## 3. Constraints

- Use only the given string.
- Do not use `input()`.
- Ignore all whitespace characters.
- Do not display whitespace characters.
- Print indexes in one horizontal line.
- Print corresponding characters directly below the indexes.
- Do not use `replace()`, `split()`, or regular expressions.

---

## 4. Think Before You Code

Before writing code, think about:

- How can we identify whitespace characters?
- How do indexes change when whitespace is ignored?
- How can two aligned rows be printed?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1

Traverse the string one character at a time.

---

### Hint 2

Use:

```python
char.isspace()
```

to check whether a character is whitespace.

---

### Hint 3

Maintain a separate counter for visible characters.

</details>

---

## 6. Learning Objectives

### Python

- Strings
- Loops
- Conditional statements
- Character processing
- `isspace()`

### Programming

- Data filtering
- Sequential indexing
- Output formatting

---

## 7. Pattern Recognition

```
Original String
        ↓
Ignore Whitespaces
        ↓
Assign Visible Indexes
        ↓
Print Index Row
Print Character Row
```

---

## 8. Core Logic

Visit every character in the string.

If the character is **not** a whitespace character:

- Print its visible index.
- Print the character.
- Increase the visible index.

---

## 9. Algorithm

1. Store the string.
2. Create a visible index counter starting from 0.
3. Traverse the string.(Read or process every character in the string from left to right, one at a time.)
4. Ignore whitespace characters.
5. Print all visible indexes.
6. Print all visible characters.
7. End.

---

## 10. Complexity

### Time Complexity

**O(n)**

where `n` is the length of the string.
The program visits each character in the string. Although there are two loops, each loop scans the string once, so the total work is proportional to the length of the string

---

### Space Complexity

**O(1)**

Only a few variables are used.
The program uses only a few extra variables (visible_index and char) regardless of the string length. It does not create another string or additional data structure.

---

## 11. Pseudocode

```text
START

Store string

visible_index = 0

FOR each character

    IF character is not whitespace

        print visible_index

        visible_index = visible_index + 1

Print newline

FOR each character

    IF character is not whitespace

        print character

END
```

---

## 12. Notes

### What are Whitespace Characters?

Whitespace characters are characters that create empty space or move the cursor, but they are **not visible** when printed.

Some common whitespace characters are:

| Character | Description |
|-----------|-------------|
| `" "` | Space |
| `"\t"` | Horizontal Tab |
| `"\n"` | New Line |
| `"\r"` | Carriage Return |
| `"\v"` | Vertical Tab |
| `"\f"` | Form Feed |

Python provides the method:

```python
char.isspace()
```

It returns:

- `True` → if the character is whitespace.
- `False` → otherwise.

Example:

```python
print(" ".isspace())    # True
print("\t".isspace())   # True
print("\n".isspace())   # True
print("A".isspace())    # False
print("5".isspace())    # False
print("@".isspace())    # False
```

For this exercise, all whitespace characters are ignored.

---

## 13. After Solving

You will understand how to:

- Process strings one character at a time.
- Ignore unwanted characters.
- Maintain custom indexes.
- Format output neatly.

---

## 14. Interview Follow-up Questions

**1. What does `isspace()` do?**

It checks whether a character is a whitespace character.

---

**2. Why do we use a separate index, visible_index = 0?**

Because whitespace characters are ignored and should not be counted. We initialize visible_index = 0 because we are manually tracking the position of only valid (non-whitespace) characters, independent of Python’s internal indexing.

---

**3. What is the time complexity?**

O(n), because each character is visited once.

---

**4. Which characters does `isspace()` detect?**

Space, tab, newline, carriage return, vertical tab, and form feed.

---

**5. Why not use `replace()`?**

This exercise is designed to practice character-by-character processing using loops and conditions.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[**solution.py**](solution.py)

</details>