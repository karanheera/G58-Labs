# PD001 - Open Your First CSV

## Problem Statement

**A company has shared an employee list stored in a CSV file named `employees.csv`.**

Your task is to read the CSV file using Pandas and display all of its contents on the screen.

Do not type the data manually.

Read it directly from the CSV file.

---

## Example

Suppose `employees.csv` contains:

| ID | Name | Department |
|----|------|------------|
| 1 | Alice | HR |
| 2 | Bob | Sales |
| 3 | Charlie | IT |

**Output**

```text
   ID     Name Department
0   1    Alice         HR
1   2      Bob      Sales
2   3  Charlie         IT
```

---

### ⚠️ Important Rule

Try solving it yourself before checking the solution.

Think on paper or in MS Word before writing code.

Ask yourself:

- Where is the data stored?
- How can Python read a CSV file?
- Once the file is read, how can I display it?

First think.

Then write the code.

---

<details>

<summary>Approach</summary>

- Import the Pandas library.
- Read the CSV file using `pd.read_csv()`.
- Store the result in a variable.
- Display the DataFrame using `print()`.

</details>

---

<details>

<summary>Algorithm</summary>

1. Import Pandas.
2. Read `employees.csv`.
3. Store it in a DataFrame.
4. Print the DataFrame.

</details>

---

<details>

<summary>Pseudocode</summary>

```text
START

Import pandas

Read employees.csv

Store in dataframe

Print dataframe

END
```

</details>

---

<details>

<summary>Complexity</summary>

### Time Complexity

Reading a CSV file requires reading every row and every column once.

If there are **n** rows in the file, Pandas processes each row while loading it.

**Overall Time Complexity: O(n)**

(where **n** is the number of rows)

### Space Complexity

The entire CSV file is loaded into memory as a DataFrame.

Therefore the memory required grows with the size of the dataset.

**Overall Space Complexity: O(n)**

</details>

---

<details>

<summary>Key Learning</summary>

- Importing Pandas
- `import pandas as pd`
- `pd.read_csv()`
- DataFrame
- `print()`

</details>

---

<details>

<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

</details>

---

## Real-World Use Case

Reading CSV files is one of the most common tasks in data analysis.

Businesses store information such as:

- Employee records
- Customer lists
- Sales reports
- Bank transactions
- Inventory data
- Website analytics

Before analyzing any data, the first step is usually reading a CSV file into Pandas.