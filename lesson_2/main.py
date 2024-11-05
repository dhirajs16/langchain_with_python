import os
from decouple import config
os.environ["GROQ_API_KEY"] = config('GROQ_API_KEY')

from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader

# llm = ChatGroq(model="llama3-8b-8192")



# 1. Webbase loader

# loader = WebBaseLoader("https://www.espn.com/")
# docs = loader.load()
# print(docs[0].page_content)



