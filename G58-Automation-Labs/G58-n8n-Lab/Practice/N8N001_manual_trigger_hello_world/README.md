# N8N001 - Manual Trigger Hello World

## Problem Statement

***Create an n8n workflow that starts manually and produces the following output.***

### Expected Output

```json
{
  "message": "Hello World"
}
```



### ⚠️ Important Rule

Try solving it yourself before checking the solution.

*How to Think About the Problem*

Before opening n8n:

- Think on paper / MS Word / notebook
- Ask yourself:
  - How does the workflow start?
  - Which node creates data?
  - What output is required?

First think, then build.

---

<details>
<summary>Approach</summary>

- Use a Manual Trigger node
- Add a Set node
- Create a field named `message`
- Assign value `Hello World`

</details>

---

<details>
<summary>Algorithm</summary>

1. Start workflow manually
2. Create a field named `message`
3. Store value `Hello World`
4. Execute workflow
5. Verify output

</details>

---

<details>
<summary>Workflow Hint</summary>

```text
Manual Trigger
      ↓
      ?
```

Which node can create custom data?

</details>

---

<details>
<summary>Key Learning</summary>

- Manual Trigger node
- Edit Fields(Set) node
- Workflow execution
- Viewing output
- Basic data creation

</details>

---

<details>
<summary>Real-World Use Case</summary>

Creating data manually is useful for:

- Testing workflows
- Learning n8n
- Debugging automations
- Creating sample data
- Prototyping larger workflows

</details>

---

<details>
<summary>Solution (Open only after trying)</summary>

Open:

[*Click Here* ](workflow.json)

</details>