# PY013 - Phone Number Cleaner

**Difficulty:** ★★☆☆☆ Beginner


## Problem Statement

A phone number is stored in a messy format with spaces and dashes.

Clean the phone number so that only digits remain.

Use the value already provided in the program.

---

### Given Data

```
Phone Number = "9876-543-210"
```

---

### Expected Output

```
Original Phone Number: 9876-543-210

Cleaned Phone Number: 9876543210
```

---

## ⭐ Key Concept (Very Important)

This program introduces **string cleaning**.

Real-world data is often messy.

Python provides tools to modify strings.

We will use:

```python
replace()
```

---

### How it works

```python
text.replace("old", "new")
```

Example:

```python
"98-76".replace("-", "")
```

Result:

```
"9876"
```

---

## Why this matters

Cleaning data is used in:

- Banking systems
- Customer databases
- Mobile applications
- Government forms
- E-commerce platforms

---

## How to Think About the Problem

Ask yourself:

- What unwanted characters are present?
- What should the final format look like?
- How can we remove or replace unwanted symbols?

---

<details>

<summary>Approach</summary>

- Store the phone number
- Remove dashes using `replace()`
- Store cleaned number
- Display both values

</details>

---

<details>

<summary>Algorithm</summary>

1. Store phone number as text
2. Replace "-" with empty string
3. Store cleaned number
4. Display original number
5. Display cleaned number

</details>

---

<details>

<summary>Pseudocode</summary>

```
START

Store phone number

Remove all "-" characters

Store cleaned number

Display original number

Display cleaned number

END
```

</details>

---

<details>

<summary>Glossary</summary>

| Term | Meaning |
|------|---------|
| string | A sequence of text |
| replace() | Replaces part of a string |
| cleaning | Removing unwanted characters |
| variable | Stores a value |
| output | Displaying information |

</details>

---

<details>

<summary>Key Learning</summary>

- Strings
- String methods
- Data cleaning
- replace() function
- Real-world formatting

</details>

---

<details>

<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

</details>

---

## Real-World Use Case

Phone number cleaning is used in:

- Banking systems
- KYC verification
- CRM tools
- WhatsApp/contact apps
- Government databases