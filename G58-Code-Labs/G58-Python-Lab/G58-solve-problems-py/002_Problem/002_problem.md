# 002 - Ask name

### Problem
Write a program that asks for a name from the user and greets the user.

---

### Output
Print exactly: for e.g.
Hello, John

<details>
<summary>Hint</summary>

Use `input()` to take user input and `print()` to display it.

</details>

<details>
<summary>Solution</summary>

```python
# solution.py

# first, we will ask the user for their name using the input() function
user_name = input('Your Name Please = ')

# then we will greet the user using the print() function
print('Hello,', user_name)