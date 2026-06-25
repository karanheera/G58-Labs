# PY002 - Ask Name and Greet


## Problem Statement
Write a program that asks the user for their name and prints a greeting message.



### Constraints
- Input will be a valid string
- Name length is assumed between 1 to 100 characters
- No empty or null input



### Input
A single string input from the user representing their name.

Example:
```

John

```



### Output
Print exactly:
```

Hello, <name>

```

Example:
```

Hello, John

```



<details>
<summary>Pattern / DSA Concept</summary>

- Pattern: Basic Input/Output
- Concept: String Manipulation
- Type: Easy / Beginner Problem

This problem does not use any advanced data structures or algorithms.

</details>



<details>
<summary>Approach</summary>

We need to:
- Take input using `input()`
- Store it in a variable
- Concatenate it with `"Hello, "`
- Print final output

</details>



<details>
<summary>Algorithm Used</summary>

- Simple Input/Output Handling
- String Concatenation

</details>



<details>
<summary>Pseudocode</summary>

```

START

READ name from user
SET result = "Hello, " + name
PRINT result

END

```

</details>



<details>
<summary>Code</summary>

```python
# 002_solution.py

user_name = input("Your Name Please = ")
print("Hello,", user_name)
```

</details>



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



<details>
<summary>Complexity</summary>

Time Complexity: O(1)

* Only one input and one print operation

Space Complexity: O(1)

* Only one variable used, no extra memory growth

In simple terms:

* Runs instantly
* Uses constant memory

</details>



<details>
<summary>Key Learning</summary>

* How to take input using `input()`
* How to print output using `print()`
* Basic string concatenation

</details>

