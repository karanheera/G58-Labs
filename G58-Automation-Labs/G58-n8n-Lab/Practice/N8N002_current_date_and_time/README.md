# N8N002 — Current Date and Time

---

## 1. Problem

Build an n8n workflow that starts manually and returns the **current date and time** when the workflow executes.

Create a field called `current_datetime` that contains the execution timestamp in ISO 8601 format.

Example:

```
2026-07-02T14:35:12.123Z
```

This introduces one of the most important concepts in automation:

**Dynamic Data (meaning: values that change every time the workflow runs.)**

Unlike the previous exercise where the output was fixed, this workflow generates fresh data during every execution.

---

## 2. Expected Output

Example:

```json
{
  "current_datetime": "2026-07-02T14:35:12.123Z"
}
```

Your timestamp will be different every time the workflow runs.

---

## 3. Constraints

* Use **Manual Trigger** to start the workflow
* Use **Edit Fields (Set)** node
* Do not use external APIs
* Do not hardcode (meaning: manually type a fixed value) the date
* Use an **Expression** to generate the current date and time
* Output must contain only one field: `current_datetime`

---

## 4. Think Before You Build

Before opening n8n, answer these questions:

* Why is today's date different every day?
* What is the difference between static data and dynamic data?
* Where does n8n obtain the current time during execution?
* Why should automations avoid hardcoded timestamps?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

* Start with **Manual Trigger**
* Add an **Edit Fields (Set)** node
* Create a field named:

```
current_datetime
```

* Instead of typing text, switch the value to an **Expression**
* Use n8n's built-in date variable to generate the current timestamp

```javascript
{{ $now }}
```

</details>

---

## 6. Learning Objectives

### n8n Basics

* Manual Trigger
* Edit Fields (Set)
* Expressions
* Dynamic values
* Workflow execution

### Core Concepts

* Current timestamp
* ISO 8601 datetime format
* Expression evaluation (meaning: n8n calculates the value while the workflow is running.)
* Runtime data (meaning: data created while the workflow executes.)

---

## 7. Workflow Pattern

```
Manual Trigger
       ↓
Edit Fields (Set)
       ↓
Current Date & Time
```

This is one of the most frequently used automation patterns because almost every production workflow records execution time.

---

## 8. Step-by-Step Execution

1. Create a Manual Trigger node.
2. Add an Edit Fields (Set) node.
3. Create a new field named:

```
current_datetime
```

4. Change the field value to an Expression.
5. Insert the built-in current datetime expression.
6. Connect both nodes.
7. Execute the workflow.
8. Inspect the generated timestamp.

---

## 9. Data Flow

### Input

```
(empty)
```

### After Manual Trigger

Workflow execution begins.

### After Edit Fields

Example:

```json
{
  "current_datetime": "2026-07-02T14:35:12.123Z"
}
```

Every execution produces a new timestamp.

---

## 10. Core Logic

The workflow works because:

* Manual Trigger starts execution.
* The Set node evaluates (meaning: calculates) an Expression.
* n8n generates the current date and time during execution.
* The generated value is stored inside a JSON field.
* The JSON object becomes the workflow output.

Unlike static text, Expressions are recalculated every time the workflow runs.

---

## 11. Common Mistakes

* Typing today's date manually instead of using an Expression
* Forgetting to switch the field to Expression mode
* Using the wrong field name
* Expecting the timestamp to remain the same after multiple executions
* Forgetting to execute the workflow

---

## 12. Debugging Steps

1. Verify the Manual Trigger is connected.
2. Confirm the field name is:

```
current_datetime
```

3. Ensure the value is an Expression, not plain text.
4. Execute the workflow.
5. Compare timestamps across multiple executions.
6. If every run shows the same value, the date was probably hardcoded.

---

## 13. Interview Questions (Realistic)

### 1. Why do we use Expressions instead of fixed values?

Expressions generate dynamic values every time the workflow executes.

---

### 2. What is dynamic data?

Data that changes while the workflow is running.

---

### 3. Why is recording timestamps important?

They help with logging, auditing, debugging, monitoring, scheduling, and tracking workflow executions.

---

### 4. What format is commonly used for dates in APIs?

ISO 8601 because it is internationally standardized and understood by most systems.

---

### 5. What happens if you execute this workflow five times?

Each execution produces a different timestamp.

---

### 6. Why shouldn't production workflows use hardcoded dates?

Because the data becomes outdated immediately and cannot represent the actual execution time.

---

### 7. What is an Expression in n8n?

An Expression allows n8n to calculate or generate values during workflow execution instead of using fixed values.

---

### 8. Can Expressions use previous node data?

Yes. Expressions can access data produced by earlier nodes in the workflow.

---

### 9. Where are timestamps commonly used in real-world automations?

* API requests
* Database records
* Audit logs
* CRM updates
* Notifications
* File naming
* Reports
* Backup systems

---

### 10. What is the main learning from this project?

Understanding how to generate dynamic runtime values using Expressions.

---

## 14. Key Takeaways

* Workflows can generate dynamic data.
* Expressions are evaluated during execution.
* ISO 8601 is the standard datetime format used by APIs.
* Timestamps are fundamental to almost every automation.
* Runtime values change every executio.

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[workflow.json](workflow.json)

*You can download this workflow.json file and import into your n8n workflow via "import a file..."*
</details>

---

## Further Reading

### Official n8n Documentation

- **Expressions**
  https://docs.n8n.io/code/expressions/

- **Edit Fields (Set) Node**
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/
