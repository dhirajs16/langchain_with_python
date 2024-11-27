# **Langchain with Python**

- **Lesson 1:** decouple lib for `.env`, groq framework for llama 3 llm model, simple llm app, chat model app with messages, prompt template.
- **Lesson 2:** realtime chat_bot(again recipe generator) with chat history.

<hr>

## **Projects**
Download necessary packages.

```
pip install django
pip install python-decouple
pip install -qU langchain-groq
```

**Project 00:** Recipe Generator.


<hr>

## **Lesson 2**

### 1. **JSON Output Parser**

```python
from langchain.output_parsers import JSONOutputParser

output_parser = JSONOutputParser()
data = {"name": "Alice", "age": 30}
result = output_parser.parse(data)
print(result)
```

**Output**:
```json
{
  "name": "Alice",
  "age": 30
}
```

### 2. **XML Output Parser**

```python
from langchain.output_parsers import XMLOutputParser

output_parser = XMLOutputParser()
data = {"name": "Alice", "age": 30}
result = output_parser.parse(data)
print(result)
```

**Output**:
```xml
<root>
  <name>Alice</name>
  <age>30</age>
</root>
```

### 3. **CSV Output Parser**

```python
from langchain.output_parsers import CSVOutputParser

output_parser = CSVOutputParser()
data = [["name", "age"], ["Alice", 30], ["Bob", 25]]
result = output_parser.parse(data)
print(result)
```

**Output**:
```
name,age
Alice,30
Bob,25
```

### 4. **Pydantic Output Parser**

```python
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class User(BaseModel):
    name: str
    age: int

output_parser = PydanticOutputParser(model=User)
data = {"name": "Alice", "age": 30}
result = output_parser.parse(data)
print(result)
```

**Output**:
```python
User(name='Alice', age=30)
```

### 5. **YAML Output Parser**

```python
from langchain.output_parsers import YAMLOutputParser

output_parser = YAMLOutputParser()
data = {"name": "Alice", "age": 30}
result = output_parser.parse(data)
print(result)
```

**Output**:
```yaml
name: Alice
age: 30
```

### 6. **Pandas DataFrame Output Parser**

```python
import pandas as pd
from langchain.output_parsers import PandasDataFrameOutputParser

output_parser = PandasDataFrameOutputParser()
data = {"name": ["Alice", "Bob"], "age": [30, 25]}
result = output_parser.parse(data)
print(result)
```

**Output**:
```
    name  age
0  Alice   30
1    Bob   25
```

### 7. **Str Output Parser**

```python
from langchain.output_parsers import StrOutputParser

output_parser = StrOutputParser()
data = "Hello, world!"
result = output_parser.parse(data)
print(result)
```

**Output**:
```
Hello, world!
```

### 8. **List Output Parser**

```python
from langchain.output_parsers import ListOutputParser

output_parser = ListOutputParser()
data = ["apple", "banana", "cherry"]
result = output_parser.parse(data)
print(result)
```

**Output**:
```
['apple', 'banana', 'cherry']
```

### 9. **Markdown List Output Parser**

```python
from langchain.output_parsers import MarkdownListOutputParser

output_parser = MarkdownListOutputParser()
data = ["item1", "item2", "item3"]
result = output_parser.parse(data)
print(result)
```

**Output**:
```markdown
- item1
- item2
- item3
```

### 10. **Numbered List Output Parser**

```python
from langchain.output_parsers import NumberedListOutputParser

output_parser = NumberedListOutputParser()
data = ["first", "second", "third"]
result = output_parser.parse(data)
print(result)
```

**Output**:
```markdown
1. first
2. second
3. third
```

<hr>

## **Lesson 3**

- packages needed to deal with pdf file for RAG application.

```bash

pip install langchain_community pypdf

```
<hr>

### **LangGraph**

**LangGraph** is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. 
- **Stateful System**: LangGraph operates like this assistant with a notebook. It remembers past interactions, tasks, and data (the "state") to provide a seamless, continuous experience. Whether it's handling a long-running process or remembering user preferences, it keeps everything organized and accessible across different sessions.

- **Agents**: Agents are like smart assistant that uses LLM models and models and other tools to make decisions and perform tasks. Unlike regular chatbots and other LLM application it doesn't directly generate text, but involves decision making as well. 



### **LangGraph Agent Simplified**
Creating a LangGraph agent involves defining various tools and actors. Here's a step-by-step analogy to make it clearer:

1. **Tools**: Think of tools as specialized instruments or functions. For example, one tool might handle calculations, another might perform searches, and another could manage data storage.
2. **Actors**: These are like the workers who use the tools. Each actor has a specific role, such as calculating results, searching for information, or interacting with the user.
3. **LLM Model**: The large language model (like GPT-4) acts as the smart supervisor. It knows which tool to use for each task based on the instructions and context.
4. **Decision Making**: When you give a task to the LangGraph agent, the LLM model decides which tool (or tools) to use to get the job done. It orchestrates the process, ensuring everything runs smoothly and efficiently.

### Example
Imagine you're running a restaurant:
- **Tools**: These are the kitchen appliances like the oven, mixer, and fridge.
- **Actors**: These are the chefs, waiters, and cleaners, each with their specific roles.
- **LLM Model (Supervisor)**: The manager decides what needs to be done—when to use the oven, who should prepare the dish, and when it should be served.
- **Decision Making**: Based on the order from a customer, the manager (LLM model) chooses the appropriate tools and actors to prepare and serve the meal.

### LangGraph in Action
So, a LangGraph agent works similarly. It utilizes various tools and actors, with the help of an LLM model, to decide which tool to pick for each task, ensuring the entire workflow is efficient and effective.

Does this analogy help clarify the concept for you? Let me know if you have any further questions!












