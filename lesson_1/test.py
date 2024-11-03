import os
from decouple import config
from langchain_groq import ChatGroq

API_KEY = config('GROQ_API_KEY')
os.environ['GROQ_API_KEY'] = API_KEY

model = ChatGroq(model="llama3-8b-8192")

query = 'just the name of the first person landed on moon'

response = model.invoke(query)

print(response.content)

# print(type(response))
# <class 'langchain_core.messages.ai.AIMessage'>