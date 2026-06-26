# PY004 - Convert Kilometers to Miles

## Problem Statement

***A distance in kilometers is given by the user. Convert it into miles and display the result.***

### Formula

```
1 kilometer = 0.621371 miles
```

---

### Example

**Input**
```
10
```

**Output**
```
Miles: 6.21371
```

---

## ⭐ Key Concept (Very Important)

This is your first program where you will:

- Take input from the user using `input()`
- Convert that input into a number using `float()`

### Why this is needed

👉 `input()` always gives **text (string)**  
👉 But we need a **number (float)** to do calculations

So we convert it like this:

```
float(input())
```

This step is very important in real programming.

---

## How to Think About the Problem

- What data does the user give?
- What type should it become for calculation?
- What formula converts km to miles?

---

<details>

<summary>Approach</summary>

- Take input in kilometers (text)
- Convert it into a number (float)
- Apply conversion formula
- Print result

</details>

---

<details>

<summary>Algorithm</summary>

1. Read input from user
2. Convert input to float
3. Multiply by 0.621371
4. Display result

</details>

---

<details>

<summary>Pseudocode</summary>

```
START

READ km (as text)
CONVERT km to number using float()

miles = km * 0.621371

PRINT miles

END
```

</details>

---

<details>

<summary>Glossary</summary>

| Term | Meaning |
|------|--------|
| input() | Gets data from user as text |
| float() | Converts text into decimal number |
| type conversion | Changing data from one type to another |
| expression | A calculation like km * 0.621371 |
| constant | A fixed value like 0.621371 |
| output | Result shown on screen |

</details>

---

<details>

<summary>Key Learning</summary>

- User input (`input()`)
- Type conversion (`float()`)
- Arithmetic expressions
- Real-world unit conversion

</details>

---

<details>

<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

</details>

---

## Real-World Use Case

Used in:

- Google Maps
- Travel apps
- Fitness apps
- Logistics systems
- Aviation and shipping