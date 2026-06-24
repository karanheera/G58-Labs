# 002 - Ask Name

---

## Problem
Write a program that asks the user for their name and prints a greeting message.

---

## Input
A single string input from the user representing their name.

Example:
```
John
```

---

## Output
Print exactly:
```
Hello, <name>
```

Example:
```
Hello, John
```

---

<details>
<summary>Approach</summary>

We need to:
- Take input from the user using `input()`
- Store it in a variable
- Combine it with the greeting string `"Hello, "`
- Print the final message

This is a simple input-output problem with string concatenation.

</details>

---

<details>
<summary>Algorithm Used</summary>

- Simple Input/Output Handling
- String Concatenation

</details>

---

<details>
<summary>Pseudocode</summary>
```
START

READ name from user
SET result = "Hello, " + name
PRINT result

END
````
</details>

---

<details>
<summary>Code</summary>
```python
# solution.py

# take user input
user_name = input('Your Name Please = ')

# print greeting message
print('Hello,', user_name)
````

</details>

---

<details>
<summary>Dry Run</summary>

Input:
```
John
```
Execution Steps:

* user_name = "John"
* print("Hello, John")

Output:
```
Hello, John
```
</details>

---

<details>
<summary>Complexity</summary>

*Time Complexity: O(1)*: 
The program performs a fixed number of operations regardless of input size. It only reads input and prints output once.

*Space Complexity: O(1)*:
No extra memory grows with input size. Only one variable (`user_name`) is used.

In simple terms:

* Runs instantly
* Uses constant memory

</details>

---

<details>
<summary>Key Learning</summary>

* How to take input using `input()` in Python
* How to print output using `print()`
* Basic string concatenation

</details>