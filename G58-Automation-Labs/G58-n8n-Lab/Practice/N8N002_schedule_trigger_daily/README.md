# N8N002 — Schedule Trigger Daily

**Difficulty:** ★☆☆☆☆ Beginner  
**Estimated Time:** 5 Minutes

---

## 1. Problem

Create an n8n workflow that starts automatically every day using a **Schedule Trigger**.

The workflow should produce the following JSON output.

---

## 2. Example

### Expected Output

```json
{
  "status": "Daily workflow executed"
}
```

---

## 3. Constraints

- Start the workflow using a **Schedule Trigger**.
- Configure the trigger to run **once every day**.
- Use an **Edit Fields (Set)** node to create the output.
- Do not use external APIs or integrations.

---

## 4. Think Before You Build

Before opening n8n, think about:

- Which node runs workflows automatically?
- How do you configure a daily schedule?
- Which node creates custom JSON data?
- What should the final output contain?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

### Hint 1

Use a **Schedule Trigger** node.

---

### Hint 2

Configure it to execute **daily**.

---

### Hint 3

Add an **Edit Fields (Set)** node.

---

### Hint 4

Create a field named:

```text
status
```

Assign it the value:

```text
Daily workflow executed
```

</details>

---

## 6. Learning Objectives

### n8n

- Schedule Trigger node
- Edit Fields (Set) node
- Workflow scheduling
- Automatic workflow execution

### Automation

- Time-based automation
- Scheduled tasks
- Creating JSON output

---

## 7. Pattern Recognition

```
Schedule Trigger
         ↓
Edit Fields (Set)
         ↓
JSON Output
```

This is the foundation of scheduled automations such as reports, reminders, and backups.

---

## 8. Core Logic

The Schedule Trigger automatically starts the workflow once every day.

The Edit Fields (Set) node creates a JSON object containing the workflow status.

---

## 9. Algorithm

1. Add a Schedule Trigger node.
2. Configure it to run daily.
3. Connect an Edit Fields (Set) node.
4. Create a field named `status`.
5. Assign the value `Daily workflow executed`.
6. Save and execute the workflow.

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

Wait for scheduled time

Create field:
    status = "Daily workflow executed"

Display output

END
```

---

## 12. Notes

| Term | Meaning |
|------|--------|
| Workflow | A sequence of connected nodes |
| Schedule Trigger | Starts a workflow at a specified time |
| Edit Fields (Set) | Creates or modifies data |
| JSON | Structured data format |
| Node | A step in a workflow |
| Schedule | Defines when the workflow runs |

---

## 13. After Solving

- Create scheduled workflows
- Configure recurring automation
- Generate custom JSON output
- Understand automatic workflow execution
- Build the foundation for time-based automations

---

## 14. Interview Follow-up Questions

**1. Why use a Schedule Trigger?**  
It automatically runs workflows at predefined times without manual intervention.

---

**2. Can a Schedule Trigger run more than once a day?**  
Yes. It can be configured with different intervals and schedules.

---

**3. What does the Edit Fields (Set) node do?**  
It creates or updates fields in the workflow data.

---

**4. Where is the schedule configured?**  
Inside the Schedule Trigger node settings.

---

**5. What are common uses of scheduled workflows?**  
Sending reports, database backups, reminders, monitoring systems, and periodic data synchronization.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[**workflow.json**](workflow.json)

</details>