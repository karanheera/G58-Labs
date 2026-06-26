# PY010 - Water Intake Tracker

**Difficulty:** ★☆☆☆☆ Beginner


## Problem Statement

A health app tracks how much water a person drinks in a day.

Calculate:

- Total water consumed
- Remaining water needed to reach the daily goal

Use the values already provided in the program.

---

### Given Data

```
Daily Goal = 3000 ml

Morning = 750 ml
Afternoon = 1000 ml
Evening = 500 ml
```

---

### Formula

```
Total Water = Morning + Afternoon + Evening

Remaining Water = Daily Goal − Total Water
```

---

### Expected Output

```
Daily Goal: 3000 ml
Total Water Consumed: 2250 ml
Remaining Water Needed: 750 ml
```

---

## ⭐ Key Concept (Very Important)

This program combines **addition** and **subtraction**.

First, several values are added together.

Then, the total is compared with the daily goal by subtracting it.

Example:

```python
total = morning + afternoon + evening

remaining = goal - total
```

Programs often perform calculations in multiple steps like this.

---

## Why this matters

Tracking progress toward a goal is common in:

- Health and fitness apps
- Nutrition trackers
- Exercise monitoring
- Habit tracking applications
- Personal wellness dashboards

---

## How to Think About the Problem

Ask yourself:

- What is the daily water goal?
- How much water was consumed during the day?
- How do we calculate the total?
- How much more water is needed?

---

<details>

<summary>Approach</summary>

- Store the daily goal
- Store the water consumed during each part of the day
- Calculate the total water consumed
- Calculate the remaining water needed
- Display the results

</details>

---

<details>

<summary>Algorithm</summary>

1. Store the daily water goal
2. Store morning, afternoon, and evening water intake
3. Calculate total water consumed
4. Calculate remaining water needed
5. Display all values

</details>

---

<details>

<summary>Pseudocode</summary>

```
START

Store daily goal

Store morning water

Store afternoon water

Store evening water

Calculate total water consumed

Calculate remaining water needed

Display daily goal

Display total water consumed

Display remaining water needed

END
```

</details>

---

<details>

<summary>Glossary</summary>

| Term | Meaning |
|------|---------|
| variable | Stores a value |
| addition | Combining multiple values |
| subtraction | Finding the difference between two values |
| total | Sum of several values |
| goal | The target value to achieve |
| output | Information displayed on the screen |

</details>

---

<details>

<summary>Key Learning</summary>

- Variables
- Addition
- Subtraction
- Arithmetic expressions
- Multi-step calculations
- Displaying results

</details>

---

<details>

<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

</details>

---

## Real-World Use Case

Water intake tracking is used in:

- Health monitoring apps
- Fitness applications
- Smartwatch health features
- Wellness platforms
- Personal habit trackers