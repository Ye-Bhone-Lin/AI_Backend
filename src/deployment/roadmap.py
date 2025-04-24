from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI
import uvicorn

load_dotenv()

model = ChatGroq(model_name="meta-llama/llama-4-scout-17b-16e-instruct")

system_prompt = """
Return with only json outputs.
{{
  "id": ,
  "title": "",
  "description": "",
  "language": "",
  "difficulty_level": "",
  "ai_generated": ,
  "steps": [
    {{
      "step_number": 1,
      "title": "",
      "description": "",
      "estimated_time_minutes": 
    }},
    {{
      "step_number": 2,
      "title": "",
      "description": "",
      "estimated_time_minutes":
    }},
    {{
      "step_number": 3,
      "title": "Frontend Framework - ",
      "description": "",
      "estimated_time_minutes": 
    }},
    {{
      "step_number": 4,
      "title": "",
      "description": ",
      "estimated_time_minutes": 
    }},
    {{
      "step_number": 5,
      "title": "",
      "description": "",
      "estimated_time_minutes":
    }}
  ]
}}
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

app = FastAPI(
    title="Roadmap API",
    version="1.0",
    description="Roadmap API"
)

add_routes(app, prompt_template | model, path = "/roadmap")

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)
