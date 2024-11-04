import os
from decouple import config
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

'''
1. config('GROQ_API_KEY'): Fetches the value of the GROQ_API_KEY from your configuration settings
(usually stored in a .env file or environment variables).

2. os.environ['GROQ_API_KEY'] = config(....): Sets this value into the OS environment variables, 
making the API key accessible throughout your program or any subprocesses it spawns.

'''
model = ChatGroq(model="llama3-8b-8192") 

# 1. Simple llm application
# query = "Who is the primeminister of Nepal?"
# response = model.invoke(query)
# print(response.content)



# 2. Chat model based application: to build conversations with messages
# messages = [
#     ('system', 'You are a standup comedian.'),
#     ('human', 'Who is the father or modern chemistry?')
# ]

# response = model.invoke(messages)
# print(response.content)
# print(type(response))  # Output: <class 'langchain_core.messages.ai.AIMessage'>



# 3. Prompt template
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")

variable_prompt = prompt_template.invoke({"topic": "cats"})

response = model.invoke(variable_prompt)

print(response.content)