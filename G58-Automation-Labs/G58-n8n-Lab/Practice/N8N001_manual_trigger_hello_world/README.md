# N8N001 — Manual Trigger Hello World

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

Create an n8n workflow that starts manually and produces the following output.

The workflow should create a JSON object containing a single field named `message`.

---

## 2. Example

### Expected Output

```json
{
  "message": "Hello World"
}
```

---

## 3. Constraints

- Start the workflow using a **Manual Trigger**.
- Use an **Edit Fields (Set)** node to create the data.
- Do not use any external APIs or integrations.
- The output must contain only the required field.

---

## 4. Think Before You Build

Before opening n8n, think about:

- Which node starts a workflow manually?
- Which node creates custom data?
- What should the final JSON look like?
- How are nodes connected?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1

Every workflow needs a starting point.

---

### Hint 2

Use the **Manual Trigger** node.

---

### Hint 3

Add an **Edit Fields (Set)** node.

---

### Hint 4

Create a field named:

```text
message
```

Assign it the value:

```text
Hello World
```

</details>

---

## 6. Learning Objectives

### n8n

- Manual Trigger node
- Edit Fields (Set) node
- Workflow execution
- Viewing execution data

### Automation

- Creating data manually
- Understanding workflow structure
- Passing data between nodes

---

## 7. Pattern Recognition

```
Manual Trigger
        ↓
Edit Fields (Set)
        ↓
JSON Output
```

This is one of the most common workflow patterns used when learning n8n.

---

## 8. Core Logic

The Manual Trigger starts the workflow.

The Edit Fields (Set) node creates a new field called `message` and assigns the value `Hello World`.

Executing the workflow returns the generated JSON.

---

## 9. Algorithm

1. Add a Manual Trigger node.
2. Connect an Edit Fields (Set) node.
3. Create a field named `message`.
4. Assign the value `Hello World`.
5. Execute the workflow.
6. Verify the output.

---

## 10. Complexity

### Time Complexity

**O(1)**

The workflow performs a fixed number of operations.

---

### Space Complexity

**O(1)**

Only one JSON field is created.

---

## 11. Pseudocode

```text
START

Wait for manual execution

Create field:
    message = "Hello World"

Display output

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Workflow | A sequence of connected nodes |
| Manual Trigger | Starts a workflow manually |
| Edit Fields (Set) | Creates or modifies data |
| JSON | Structured data format |
| Node | A single step in a workflow |
| Execution | Running the workflow |

---

## 13. After Solving

- Understand how workflows begin
- Create custom JSON data
- Execute workflows manually
- Inspect node outputs
- Prepare for larger automations

---

## 14. Interview Follow-up Questions

**1. Why do we use a Manual Trigger?**  
It allows the workflow to be started manually for testing and learning.

---

**2. What does the Edit Fields (Set) node do?**  
It creates new fields or updates existing data.

---

**3. Can a workflow have multiple trigger nodes?**  
No. Only one trigger starts a workflow execution.

---

**4. Why is JSON used in n8n?**  
Most nodes exchange data using JSON objects.

---

**5. Where is the workflow output visible?**  
In the execution results after running the workflow.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[**workflow.json**](workflow.json)

</details>