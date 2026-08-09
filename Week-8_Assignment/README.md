
# 🤖 Single Agent Systems & Agent Pipelines

## Week 8 – Celebal Technologies Data Science Internship

A beginner-friendly implementation of a **Single-Agent Smart Assistant** using Python. The project demonstrates the fundamental concepts of agentic AI systems, including **conditional routing, tool integration, structured outputs, and basic error handling**.

The agent receives a user's query, identifies the type of request using rule-based conditions, selects the appropriate tool when required, executes the task, and returns the result in a structured format.

---

## 👨‍💻 Author

**Priyanshu Pratik**

Data Science Intern  
Celebal Technologies

---

## 📌 Project Overview

The objective of this project is to understand the basic architecture of a **single-agent pipeline** and implement a simple intelligent assistant capable of handling different types of user queries.

Instead of processing every query in the same way, the agent uses **conditional routing** to determine the most appropriate action.

The implemented system supports three primary query categories:

1. **Mathematical Queries** → Calculator Tool
2. **Keyword Extraction Queries** → Keyword Extraction Tool
3. **General Queries** → Direct General Response

The project demonstrates how an agent can act as a controller that receives a query, determines its intent, selects an appropriate tool, executes the required operation, and produces a structured response.

---

## 🎯 Problem Statement

Build a **Single-Agent Smart Assistant** that:

- Understands user queries
- Routes tasks based on query intent
- Uses tools when required
- Returns structured JSON-style output
- Handles basic errors gracefully

The agent is designed to handle the following types of requests:

| Query Type | Action |
|------------|--------|
| Mathematical query | Calculator Tool |
| Keyword extraction query | Keyword Extraction Tool |
| General query | Direct Response |

---

## 🧠 Concepts Demonstrated

This project focuses on the following concepts of agentic AI:

- Single-agent systems
- Agent pipelines
- Conditional routing
- Rule-based intent detection
- Tool integration
- Structured outputs
- Error handling
- Interactive agent execution
- Test-driven validation of agent behavior

---

## 🏗️ Agent Architecture

The basic workflow of the project is:

```text
User Query
    |
    v
Single Agent
    |
    v
Query Analysis
    |
    +-----------------------+
    |           |           |
    v           v           v
Calculate    Keywords    General
    |           |           |
    v           v           v
Calculator   Keyword      Direct
Tool         Extractor    Response
    |           |           |
    +-----------+-----------+
                |
                v
        Structured Response
````

The agent acts as the central controller of the workflow. It examines the incoming query and determines which processing path should be followed.

---

# 🛠️ Tools Implemented

## 1. Calculator Tool

The Calculator Tool is responsible for evaluating mathematical expressions.

### Function

```python
def calculator(expression: str) -> str:
```

### Purpose

It receives a mathematical expression and returns the calculated result.

### Example

Input:

```text
20 + 5
```

Output:

```text
25
```

The tool also includes basic exception handling so that invalid mathematical expressions do not cause the complete program to terminate.

---

## 2. Keyword Extraction Tool

The Keyword Extraction Tool extracts potentially important words from a given text.

### Function

```python
def extract_keywords(text: str) -> list:
```

### Purpose

The tool:

1. Splits the input text into individual words.
2. Converts the words to lowercase.
3. Filters words based on their length.
4. Removes duplicate words.
5. Returns a maximum of five keywords.

### Example

Input:

```text
Artificial Intelligence is transforming industries
```

Possible output:

```text
[
    "artificial",
    "intelligence",
    "transforming",
    "industries"
]
```

The exact ordering of keywords may vary because the implementation uses a set to remove duplicate values.

---

# 🤖 Agent Logic

The `agent()` function is the central component of the project.

Its main responsibilities are:

1. Receive the user's query.
2. Convert the query to lowercase for easier matching.
3. Identify the query category.
4. Route the query to the appropriate tool.
5. Execute the selected operation.
6. Return the result in a structured format.
7. Handle unexpected errors.

The agent follows a simple rule-based routing strategy.

### Routing Rules

```text
If query contains "calculate"
        ↓
Calculator Tool

If query contains "keywords"
        ↓
Keyword Extraction Tool

Otherwise
        ↓
General Response
```

This demonstrates the concept of **conditional routing**, which is an important component of agent pipelines.

---

# 🔀 Conditional Routing

Conditional routing allows the agent to choose different actions depending on the input query.

For example:

### Query

```text
Calculate 20 + 5
```

The agent identifies the word `calculate` and routes the query to the Calculator Tool.

---

### Query

```text
Extract keywords from Artificial Intelligence is transforming industries
```

The agent identifies the keyword-related request and routes it to the Keyword Extraction Tool.

---

### Query

```text
What is machine learning?
```

The query does not match either of the defined tool conditions, so it is handled as a general query.

This simple routing mechanism demonstrates how an agent can dynamically choose between different processing paths.

---

# 📦 Structured Output

The agent returns responses using a dictionary structure that follows a JSON-like format.

The basic response structure is:

```json
{
    "type": "...",
    "result": "..."
}
```

The `type` field identifies the category of the operation, while the `result` field contains the output.

### Calculation Response

```json
{
    "type": "calculation",
    "result": "25"
}
```

### Keyword Response

```json
{
    "type": "keywords",
    "result": [
        "artificial",
        "intelligence",
        "industries"
    ]
}
```

### General Response

```json
{
    "type": "general",
    "result": "You asked: What is machine learning?"
}
```

### Error Response

```json
{
    "type": "error",
    "result": "..."
}
```

Structured responses make the output predictable and easier for other components or applications to process.

---

# ⚠️ Error Handling

Basic error handling has been implemented using Python's `try-except` mechanism.

The Calculator Tool catches errors that may occur while evaluating an expression.

The agent itself also uses exception handling so that unexpected failures can be returned as a structured error instead of abruptly terminating the workflow.

This improves the basic reliability and robustness of the application.

---

# 🧪 Testing

The project includes predefined test cases to verify whether the routing logic works correctly.

### Test Case 1 – Mathematical Query

```text
Calculate 20 + 5
```

Expected behavior:

```text
Route → Calculator Tool
Result → 25
```

---

### Test Case 2 – Keyword Extraction

```text
Extract keywords from Artificial Intelligence is transforming industries
```

Expected behavior:

```text
Route → Keyword Extraction Tool
Result → Extracted keywords
```

---

### Test Case 3 – General Query

```text
What is machine learning?
```

Expected behavior:

```text
Route → General Response
Result → General response
```

All three test cases were executed successfully in the Colab notebook.

---

# 💻 Interactive Mode

The project also provides an interactive mode that allows users to continuously enter queries.

The user can enter different requests without manually calling the `agent()` function each time.

Example:

```text
Enter query (type 'exit' to stop): Calculate 50 * 4

Response:
{'type': 'calculation', 'result': '200'}
```

Another example:

```text
Enter query (type 'exit' to stop): What is Python?

Response:
{'type': 'general', 'result': 'You asked: What is Python?'}
```

The interactive session can be terminated by entering:

```text
exit
```

---

# 🔄 Complete Workflow

The complete execution flow of the application is:

### Step 1 – User Input

The user enters a natural-language query.

### Step 2 – Query Normalization

The query is converted to lowercase to make keyword matching case-insensitive.

### Step 3 – Intent-Based Routing

The agent checks the query against predefined routing conditions.

### Step 4 – Tool Selection

The appropriate tool is selected based on the identified query type.

### Step 5 – Tool Execution

The selected tool processes the request.

### Step 6 – Error Handling

If an error occurs during processing, it is captured and returned appropriately.

### Step 7 – Structured Response

The agent returns the final result using a structured response containing the type and result.

---

# 🧰 Technology Stack

| Technology             | Purpose                               |
| ---------------------- | ------------------------------------- |
| Python                 | Core programming language             |
| Google Colab           | Development and execution environment |
| Python Functions       | Tool implementation                   |
| Conditional Logic      | Query routing                         |
| Exception Handling     | Error management                      |
| JSON-like Dictionaries | Structured responses                  |

---

# 📁 Project Structure

The project can be organized as:

```text
Single-Agent-Pipeline/
│
├── week_8_assignment.ipynb
│
└── README.md
```

### `week_8_assignment.ipynb`

Contains:

* Problem statement
* Calculator Tool
* Keyword Extraction Tool
* Agent implementation
* Conditional routing
* Test cases
* Interactive mode

### `README.md`

Contains the project documentation, implementation details, architecture, and usage information.

---

# ▶️ How to Run the Project

## Option 1 – Google Colab

1. Open the provided notebook in Google Colab.
2. Run the Calculator Tool cell.
3. Run the Keyword Extraction Tool cell.
4. Implement and run the Agent Logic cell.
5. Run the Test Cases cell.
6. Run the Interactive Mode cell.
7. Enter queries and observe the responses.

---

## Option 2 – Local Jupyter Notebook

The notebook can also be downloaded and executed locally using Jupyter Notebook or JupyterLab.

Make sure Python is installed on the system and then open:

```text
week_8_assignment.ipynb
```

Run the cells sequentially.

---

# 📊 Example Execution

### Input

```text
Calculate 20 + 5
```

### Agent Decision

```text
Intent → Calculation
Tool → Calculator
```

### Output

```json
{
    "type": "calculation",
    "result": "25"
}
```

---

### Input

```text
Extract keywords from Artificial Intelligence is transforming industries
```

### Agent Decision

```text
Intent → Keyword Extraction
Tool → Keyword Extractor
```

### Output

```json
{
    "type": "keywords",
    "result": [
        "transforming",
        "intelligence",
        "industries",
        "artificial"
    ]
}
```

---

### Input

```text
What is machine learning?
```

### Agent Decision

```text
Intent → General
Tool → None
```

### Output

```json
{
    "type": "general",
    "result": "You asked: What is machine learning?"
}
```

---

# 🎓 Learning Outcomes

Through this project, the following concepts were implemented and understood:

* Understanding the basic architecture of an agent pipeline.
* Understanding how a single agent can control multiple tools.
* Implementing rule-based conditional routing.
* Integrating specialized tools into an agent.
* Creating structured responses.
* Handling errors using exception handling.
* Testing different query types.
* Implementing an interactive agent interface.
* Understanding how agent workflows can be extended with additional tools.

---

# 🚀 Future Enhancements

The current implementation intentionally focuses on the core requirements of the Week-8 assignment. The architecture can be extended into a more advanced agentic AI application.

Possible future improvements include:

* LLM-based intent detection
* More advanced natural-language understanding
* Additional tools such as summarization and unit conversion
* Improved mathematical expression handling
* Better keyword extraction using NLP techniques
* Tool selection using an LLM
* Logging and monitoring
* More robust input validation
* Conversation memory
* Streamlit-based web interface
* API-based backend
* Cloud deployment
* Authentication
* Persistent conversation history

These enhancements can transform the basic educational pipeline into a more production-oriented multi-tool AI assistant.

---

# 🔐 Note on the Calculator Implementation

The educational version of this project uses Python's `eval()` function inside the Calculator Tool to demonstrate basic expression evaluation.

For a production application, unrestricted evaluation of user-provided expressions should not be used because of security concerns.

A production-level implementation should use a safer mathematical expression parser or a restricted evaluation mechanism.

---

# 📌 Key Takeaway

This project demonstrates the fundamental idea behind a tool-using agent:

> **The agent receives a user query, determines its intent, conditionally routes the query to the appropriate tool, executes the required operation, handles errors, and returns a structured response.**

Although the implementation is intentionally simple, it establishes the core concepts required to understand more advanced agentic AI architectures.

---

## 👨‍💻 Author

**Priyanshu Pratik**

Data Science Intern
**Celebal Technologies**

---

## 📚 Internship

**Celebal Technologies – Data Science Internship**

**Week 8 Assignment: Single Agent Systems & Agent Pipelines**

```
```

