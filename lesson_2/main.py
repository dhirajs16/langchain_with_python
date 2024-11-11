from langchain_groq import ChatGroq
from decouple import config

groq_api_key = config('GROQ_API_KEY')
llm = ChatGroq(groq_api_key=groq_api_key, model='llama3-8b-8192')

messages = [
    # ('system', """
    #  You are a simple recipe generator. If queries other than recipe generation and food
    #  are asked then just reply "I'm a simple recipe generator. I can't help you with this."
    #  """),
    ('system', 'You are a simple AI assistant.'),
]

def chat_bot(query):
    messages.append(('human', query))
    response = llm.invoke(messages)
    print('AI:', response.content)
    messages.append(('ai', response.content))

while True:
    query = input('You: ')
    if query.lower() in ('exit', 'quit'):
        break
    
    chat_bot(query)
