from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI
import uvicorn

load_dotenv()

model = ChatGroq(model_name="LLama3-70b-8192")

system_prompt = """
**Explain details about the step and add more resources.**
**Dont provide another steps.**
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

app = FastAPI(
    title="Explain Details API",
    version="1.0",
    description="Explain Details API"
)

add_routes(app, prompt_template | model, path = "/steps")

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)
