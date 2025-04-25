from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI
import uvicorn

load_dotenv()

model = ChatGroq(model_name="LLama3-70b-8192")

system_prompt = """
Return Output Json only. Add {{input: [], expectedOutput: }}, {{input: [], expectedOutput: }} within testCases session,
{{
  "id": ,
  "title": ,
  "description": ,
  "timeLimit": ,
  "testCases": [
  ],
  "hint": ,
  "solution": {{
    "javascript": ,
    "python": ,
    "c": 
  }},
  "sampleInput": {{
    "javascript": ,
    "python": ,
    "c":   }}
}},
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

add_routes(app, prompt_template | model, path = "/formatcode")

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)