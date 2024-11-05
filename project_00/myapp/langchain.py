import os
from decouple import config
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

model = ChatGroq(model = 'mixtral-8x7b-32768')

def recipe_generator(recipe):
    prompt_template = ChatPromptTemplate([
            ("system", "You are a Recipe Generator Assistant. You have answer only food recipe recipe related query."),
            ("user", "Tell me the step by step recipe of {topic}")
    ])

    variable_prompt = prompt_template.invoke({"topic": recipe})
    
    response = model.invoke(variable_prompt)
    return response.content