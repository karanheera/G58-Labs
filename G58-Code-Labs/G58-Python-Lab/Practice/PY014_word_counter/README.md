# PY014 — Word Counter

**Difficulty:** ★★☆☆☆ Beginner  
**Estimated Time:** 7 Minutes

---

## 1. Problem

Given a sentence, count the total number of words present in it.

Use the sentence already provided in the program.

---

## 2. Example

### Input (Given Data)

```text
I am the best and I love myself
```

### Output

```text
Sentence: I am the best and I love myself

Word Count: 8
```

---

## 3. Constraints

- Use only the given sentence.
- Count words using built-in string methods.
- Do not use `input()`, loops, or user-defined functions.

---

## 4. Think Before You Code

Before writing any code, think about:

- What separates words in a sentence?
- Which Python method converts a sentence into individual words?
- How can you count the number of items in a list?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1

Words are usually separated by spaces.

---

### Hint 2

Use the `split()` method.

---

### Hint 3

Use the `len()` function to count the words.

</details>

---

## 6. Learning Objectives

### Python

- String methods
- `split()`
- `len()`

### Programming

- Counting data
- Working with lists
- Basic text processing

---

## 7. Pattern Recognition

```
Sentence
      ↓
Split into Words
      ↓
Count Total Words
```

This pattern is commonly used in text processing and data analysis.

---

## 8. Core Logic

The `split()` method divides a sentence into a list of words.

The `len()` function counts how many words are in that list.

---

## 9. Algorithm

1. Store a sentence
2. Split the sentence into words
3. Count the words using `len()`
4. Print the sentence
5. Print the word count

---

## 10. Complexity

### Time Complexity

**O(n)**

Where `n` is the length of the sentence.

---

### Space Complexity

**O(n)**

A list of words is created after splitting the sentence.

---

## 11. Pseudocode

```text
START

Store a sentence

Split the sentence into words

Count the number of words

Print the sentence

Print the word count

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| string | Text data |
| split() | Breaks a string into words, default sep = whitespace |
| list | Collection of items |
| len() | Counts the number of items |
| word | Individual text separated by spaces |
| variable | Stores a value |

---

## 13. After Solving

- Work with string methods
- Count words in text
- Understand lists
- Learn basic text processing

---

## 14. Interview Follow-up Questions

**1. What does `split()` return?**  
It returns a list containing the words of the string.

---

**2. Why do we use `len()`?**  
It returns the total number of items in the list.

---

**3. What is the default separator in `split()`?**  
Whitespace (spaces, tabs, newlines).

---

**4. What happens if there are multiple spaces between words?**  
`split()` automatically handles multiple spaces correctly.

---

**5. Can words be counted without `split()`?**  
Yes, by manually checking spaces using loops, but `split()` is simpler and more readable.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[**solution.py**](solution.py)

</details>