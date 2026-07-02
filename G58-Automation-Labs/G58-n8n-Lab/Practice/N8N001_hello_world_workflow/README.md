# N8N001 — Manual Trigger Hello World

---

## 1. Problem

Build your first n8n workflow that starts manually and produces a simple JSON output.

You will create a single field called `message` with the value:

```

Hello World

````

This is the foundation of all workflows in n8n.

---

## 2. Expected Output

```json
{
  "message": "Hello World"
}
````

---

## 3. Constraints

* Use **Manual Trigger** to start the workflow
* Use **Edit Fields (Set)** node to create data
* Do not use APIs or external services
* Output must contain only one field: `message`

---

## 4. Think Before You Build

Before opening n8n, answer:

* What starts a workflow?
* How do we create data inside n8n?
* What will the final JSON look like?
* How do nodes pass data between each other?

---

## 5. Hints

<details>

<summary>Need a Hint?</summary>

* Every workflow needs a starting point
* Use **Manual Trigger**
* Use **Edit Fields (Set)** node
* Create a field called `message`
* Set value to `Hello World`

</details>

---

## 6. Learning Objectives

### n8n Basics

* Manual Trigger node
* Edit Fields (Set) node
* Workflow execution
* Data inspection

### Core Concepts

* JSON structure
* Node-to-node data flow
* Output visualization

---

## 7. Workflow Pattern

```
Manual Trigger
      ↓
Edit Fields (Set)
      ↓
Output JSON
```

This is the most basic automation pattern in n8n.

---

## 8. Step-by-Step Execution

1. Add Manual Trigger node
2. Add Edit Fields (Set) node
3. Create field: `message`
4. Set value: `Hello World`
5. Connect nodes
6. Execute workflow
7. Check output in execution panel

---

## 9. Data Flow

### Input

```
(empty)
```

### After Set Node

```json
{
  "message": "Hello World"
}
```

---

## 10. Core Logic

The workflow works because:

* Manual Trigger starts execution
* Set node creates structured data
* n8n passes data forward automatically
* Execution panel shows final output

---

## 11. Common Mistakes

* Forgetting to connect nodes
* Not executing workflow
* Expecting auto-run behavior
* Wrong field name (message ≠ Message)
* Not checking execution output

---

## 12. Debugging Steps

1. Check node connections
2. Click Execute Workflow
3. Open execution view
4. Inspect JSON output
5. Fix field names if needed

---

## 13. Interview Questions (Realistic)

### 1. What happens when you execute this workflow?

The Manual Trigger starts execution and data flows through the Set node to output JSON.

---

### 2. Why do we use a Set node here?

To create structured data inside the workflow.

---

### 3. What will happen if we remove the Manual Trigger?

The workflow will not start.

---

### 4. How does data move in n8n?

Data moves node-by-node in JSON format.

---

### 5. What is the output of this workflow used for in real systems?

It is used to test workflow execution before building real automations.

---

### 6. What is the most common mistake beginners make here?

Not connecting nodes or expecting automatic execution.

---

### 7. How would you modify this workflow for real use?

Replace Manual Trigger with Webhook or Cron trigger.

---

### 8. Why is JSON important in n8n?

Because every node communicates using JSON objects.

---

### 9. Can this workflow handle multiple messages?

Not in current form; it only creates one static field.

---

### 10. What is the main learning from this project?

Understanding how a workflow starts, processes data, and produces output.

---

## 14. Key Takeaways

* Every workflow starts with a trigger
* Set node creates data
* JSON is the core data format
* Execution is step-by-step
* Output is visible in execution panel

---

## 15. Solution

<details>

<summary>Solution (Open only after trying)</summary>

[workflow.json](workflow.json)

*You can download this workflow.json file and import into your n8n workflow via "import a file..."*
</details>
