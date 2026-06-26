# PY001 - Print Personal Greeting
**Difficulty:** ★☆☆☆☆ Beginner

## Problem Statement
***Write a program that asks the user for their name and prints a greeting message.***

### Example

**Input**

```text
John
```

**Output**

```text
Hello, John
```


### ⚠️ Important Rule
Try solving it yourself before checking the solution.

*How to Think About the Problem*

Before coding:

- Think on paper / MS Word / notebook
- Ask yourself:
  - What is input?
  - What is output?
  - How do I connect them?*

First think, then code on plain paper or MS word or Google Doc


---

<details>
<summary>Approach</summary>

- Take input using `input()`
- Store it in a variable
- Print `"Hello, " + name`
</details>

---

<details>
<summary>Algorithm</summary>

1. Read input from user  
2. Store in variable  
3. Print greeting message  
</details>

---

<details>
<summary>Pseudocode</summary>

```
START
READ name
PRINT "Hello, " + name
END
```

</details>

---

<details>
<summary>Complexity</summary>

*Time Complexity*

`input()` reads the user's input. If the input length is `n` characters, reading it takes `O(n)` time.

`print("Hello,", name)` outputs the greeting and the input string, which also takes `O(n)` time because it prints the entire input.

**Overall Time Complexity: `O(n)`**

(where `n` is the length of the input string)

*Space Complexity*

The variable `name` stores the input string of length `n`, requiring `O(n)` space.

No other data structures grow with input size.

**Overall Space Complexity: `O(n)`**

(Simple and constant operations only)

</details>

---

<details>
<summary>Key Learning</summary>

- input() function
- print() function
- string concatenation
</details>

---

<details>
<summary>Solution (Open only after trying)</summary>

To Open Solution:
[*Click Here* ](solution.py)


</details>

---

### Real-World Use Case

Greeting users is commonly used in:
- Login systems
- Customer portals
- Chatbots
- Desktop applications
- Web applications