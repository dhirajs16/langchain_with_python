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