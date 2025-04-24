from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI
import uvicorn

load_dotenv()

model = ChatGroq(model_name="LLama3-70b-8192")

system_prompt = """
You are an assistant that only explains the *description* of a course. 

If the user asks a question related to the course *description*, explain it in detail and provide **resources**.
If the user's question is not related to the *description* *Show the Title and give him example questions., explain in a way that user can understand based on the level user currently at.*
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