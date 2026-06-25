# FAP001 - Create Simple Hello World API (FastAPI)

## Problem Statement

***Create your first FastAPI application that returns a simple greeting message when accessed in the browser.***


## Example

### Request

Open in browser:

```text
http://127.0.0.1:8000/
```

### Response

```json
{
  "message": "Hello, World"
}
```

---

## ⚠️ Important Rule

Try solving it yourself before checking the solution.

*How to Think About the Problem*

Before coding:

* Think on paper / notebook
* Ask yourself:

  * What is an API?
  * What is a URL?
  * What happens when a browser hits a server?

First think, then code.

---

<details>
<summary>Approach</summary>

* Import FastAPI
* Create app instance
* Define a GET route `/`
* Return a JSON response

</details>

---

<details>
<summary>Algorithm</summary>

1. Import FastAPI
2. Create FastAPI app
3. Define GET endpoint `/`
4. Return dictionary response
5. Run server

</details>

---

<details>
<summary>Pseudocode</summary>

```
START
IMPORT FastAPI
CREATE app
DEFINE route "/"
    RETURN {"message": "Hello, World"}
END
```
</details>

---

<details>
<summary>Complexity</summary>

*Time Complexity*

The API always returns a fixed response, so execution is constant.

**O(1)**


*Space Complexity*

Only a small JSON object is returned.

**O(1)**

</details>

---

<details>
<summary>Key Learning</summary>

* What is FastAPI
* Creating first API
* GET request handling
* JSON response structure
* Running server using uvicorn

</details>

---

<details>
<summary>Solution (Open only after trying)</summary>

To Open Solution:

[*Click Here*](solution.py)

```text
Run:
uvicorn solution:app --reload
```

</details>

---

## Real-World Use Case

This kind of API is used in:

* Health check endpoints (`/health`)
* Backend service testing
* Microservice startup checks
* Server status APIs