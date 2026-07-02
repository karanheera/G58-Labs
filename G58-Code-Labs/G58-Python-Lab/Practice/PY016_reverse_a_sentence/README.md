# PY016 — Reverse a Sentence

**Difficulty:** ★★☆☆☆ Beginner  
**Estimated Time:** 8 Minutes

---

## 1. Problem

Given a sentence, display it in reverse order.

Use the sentence already provided in the program and reverse all of its characters using Python string slicing.

Display:

- Original sentence
- Reversed sentence

---

## 2. Example

### Input (Given Data)

```text
Sentence = Python is fun
```

### Output

```text
Original Sentence: Python is fun

Reversed Sentence: nuf si nohtyP
```

---

## 3. Constraints

- Use only the given sentence.
- Do not use `input()`.
- Do not use loops.
- Do not use functions for reversing like `reversed()`.
- Reverse the sentence using string slicing.

---

## 4. Think Before You Code

Before writing any code, think about:

- How can a string be read from the last character to the first?
- Does Python slicing allow moving backwards?
- What does a negative step mean in slicing?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1

String slicing has three parts.

```python
text[start:end:step]
```

---

### Hint 2

Normally the step is positive.

Example:

```python
text[0:5:1]
```

moves from left to right.

---

### Hint 3

A negative step moves in the opposite direction.

```python
text[::-1]
```

reads the string from the last character to the first.

</details>

---

## 6. Learning Objectives

### Python

- String slicing
- Negative indexing
- Slice step value
- Variables
- Printing output

### Programming

- Reversing data
- Reading sequences in reverse order
- Understanding traversal direction
- Working with immutable (cannot be changed after creation) strings

---

## 7. Pattern Recognition

```
Original Data
      ↓
Reverse Direction
      ↓
Create New String
      ↓
Display Result
```

This pattern appears in many real-world applications such as:

- Palindrome checking
- Data processing
- Encryption techniques
- Text manipulation
- Algorithm design

---

## 8. Core Logic

Python strings support slicing.

When the slice step is **-1**, Python starts from the last character and moves backwards one character at a time until the beginning of the string.

```python
text[::-1]
```

This creates a new reversed string while leaving the original string unchanged.

---

## 9. Algorithm

1. Store the sentence.
2. Reverse it using slicing with step `-1`.
3. Store the reversed sentence.
4. Print the original sentence.
5. Print the reversed sentence.

---

## 10. Complexity

### Time Complexity

**O(n)**

Where **n** is the number of characters in the string.

### Why?

Python creates a brand-new string containing every character in reverse order.

Each character is copied exactly once into the new string.

Therefore, the execution time increases linearly with the size of the string.

---

### Space Complexity

**O(n)**

### Why?

Strings in Python are immutable (cannot be modified after creation).

When reversing a string, Python creates a completely new string of the same size.

Therefore, the extra memory required grows with the number of characters.

---

## 11. Pseudocode

```text
START

Store sentence

Reverse sentence using slicing

Print original sentence

Print reversed sentence

END
```

---

## 12. Notes

| Term | Meaning |
|------|---------|
| string | A sequence of characters |
| slicing | Extracting part (or all) of a string using indexes |
| step | Number of positions moved during slicing |
| negative step | Moves from right to left |
| immutable | Cannot be modified after creation |
| reverse | Arrange characters in opposite order |
| index | Position of a character inside a string |

---

## 13. Python Documentation

### String Slicing

Official Python Documentation:

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

Python sequences (including strings) support slicing using:

```python
sequence[start:end:step]
```

Examples:

```python
text = "Python"

print(text[::1])
print(text[::-1])
```

Output

```text
Python
nohtyP
```

---

## 14. After Solving

You should now understand how to:

- Reverse a string
- Use negative step values
- Read strings from right to left
- Apply slicing in different ways
- Work with immutable strings
- Understand how slicing creates new strings

---

## 15. Interview Follow-up Questions

### 1. What does `[::-1]` mean?

It creates a slice of the entire string while moving backwards one character at a time.

---

### 2. Why is the step `-1`?

Because Python moves from the end of the string toward the beginning.

---

### 3. Does reversing change the original string?

No.

A new string is created because strings are immutable.

---

### 4. What is the time complexity of reversing using slicing?

**O(n)** because every character is copied into a new string.

---

### 5. What is the space complexity?

**O(n)** because a new string of equal length is created.

---

### 6. Can we reverse using loops?

Yes.

Characters can be traversed (meaning: visited one by one) from the end toward the beginning.

---

### 7. What is the difference between negative indexing and a negative step?

Negative indexing refers to positions from the end (like `text[-1]`).

A negative step controls the direction of traversal during slicing.

---

### 8. What happens if the string is empty?

The reversed string is also empty.

No error occurs.

---

### 9. Can `[::-1]` reverse lists?

Yes.

It works with many Python sequences including lists and tuples.

---

### 10. Where is string reversal used in real applications?

Examples include:

- Palindrome detection
- Data transformation
- Cryptography
- Text processing
- Algorithm practice

---

## 16. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[**solution.py**](solution.py)

</details>