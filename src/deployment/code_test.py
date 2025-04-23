from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from fastapi import FastAPI
import uvicorn
from langserve import add_routes
from operator import itemgetter

load_dotenv()
model = ChatGroq(model_name="meta-llama/llama-4-scout-17b-16e-instruct")

template1 = """
You are a code reviewer.
- You have to give the code test based on user level.
- You have to give the user to code test which can be all programming languages but you dont have to MENTION.
After that give them a feedback.
- Check their logic step-by-step.
- If the code is incorrect or incomplete, explain where it breaks and how to fix it.
- If the code is mostly correct, provide helpful suggestions to improve.
- Be friendly and constructive.
Say goodbyes.
---
Question: {question}
"""
prompt1 = ChatPromptTemplate.from_template(template1)

app = FastAPI(
    title="CodeTest API",
    version="1.0",
    description="CodeTest API"
)

add_routes(app, prompt1 | model, path="/codetest")

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)
