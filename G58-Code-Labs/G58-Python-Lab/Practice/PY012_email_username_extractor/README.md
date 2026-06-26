# PY012 - Email Username Extractor

**Difficulty:** ★★☆☆☆ Beginner


## Problem Statement

An email address contains two parts:

- Username
- Domain

Extract and display only the **username** from the email address.

Use the value already provided in the program.

---

### Given Data

```
Email = john.smith@gmail.com
```

---

### Expected Output

```
Email: john.smith@gmail.com

Username: john.smith
```

---

## ⭐ Key Concept (Very Important)

This program introduces **string slicing**.

A string is made up of individual characters.

Python lets us extract part of a string using slicing.

Example:

```python
email = "john@gmail.com"

username = email[:4]
```

Slicing follows this pattern:

```python
text[start:end]
```

- `start` → where to begin
- `end` → where to stop (not included)

---

## Why this matters

Working with parts of text is common in:

- Login systems
- Registration forms
- Email applications
- Customer databases
- User account management

---

## How to Think About the Problem

Ask yourself:

- What information is stored in the email?
- Which part do we need?
- How can we extract only the username?

---

<details>

<summary>Approach</summary>

- Store the email address
- Extract the username using string slicing
- Store the extracted username
- Display both values

</details>

---

<details>

<summary>Algorithm</summary>

1. Store the email address
2. Extract the username portion
3. Store the username
4. Display the email
5. Display the username

</details>

---

<details>

<summary>Pseudocode</summary>

```
START

Store email address

Extract username

Store username

Display email

Display username

END
```

</details>

---

<details>

<summary>Glossary</summary>

| Term | Meaning |
|------|---------|
| string | A sequence of text |
| character | A single letter, number, or symbol |
| slicing | Extracting part of a string |
| index | Position of a character in a string |
| variable | Stores a value |
| output | Information displayed on the screen |

</details>

---

<details>

<summary>Key Learning</summary>

- Strings
- String slicing
- Index positions
- Variables
- Displaying text

</details>

---

<details>

<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

</details>

---

## Real-World Use Case

Username extraction is used in:

- Email applications
- User registration systems
- Login portals
- CRM software
- Customer management systems