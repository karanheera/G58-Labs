# PY001 - Print Personal Greeting

---

## 🧠 Problem Statement
Write a program that asks the user for their name and prints a greeting message.

---

## 📥 Input
A single string input from the user.

Example:

John


---

## 📤 Output
Print exactly:


Hello, <name>


Example:

Hello, John


---

## ⚠️ Important Rule
Try solving it yourself before checking the solution.

---

<details>
<summary>🧠 How to Think About the Problem</summary>

Before coding:

- Think on paper / MS Word / notebook
- Ask yourself:
  - What is input?
  - What is output?
  - How do I connect them?

👉 First think, then code.
</details>

---

<details>
<summary>🪜 Approach</summary>

- Take input using `input()`
- Store it in a variable
- Print `"Hello, " + name`
</details>

---

<details>
<summary>🧾 Algorithm</summary>

1. Read input from user  
2. Store in variable  
3. Print greeting message  
</details>

---

<details>
<summary>📌 Pseudocode</summary>


START
READ name
PRINT "Hello, " + name
END

</details>

---

<details>
<summary>⏱ Complexity</summary>

- Time Complexity: O(1)
- Space Complexity: O(1)

(Simple and constant operations only)
</details>

---

<details>
<summary>🎯 Key Learning</summary>

- input() function
- print() function
- string concatenation
</details>

---

<details>
<summary>💡 Solution (Open only after trying)</summary>

```python
name = input()
print("Hello,", name)
``` id="sol001"
</details>