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
    id: 1,
    question: "",
    options: ["","","",""
    ],
    correctAnswer: "",
    explainAnswer: "",
  }},
  {{
    id: 2,
    question: "",
    options: [],
    correctAnswer: "",    
    explainAnswer: "",
  }},
  {{
    id: 3,
    question: "",
    options: [
      "",
      "",
      "",
      "",
    ],
    correctAnswer: "",
    explainAnswer: "",
  }},
  {{
    id: 4,
    question: "",
    options: ["", "", "", ""],
    correctAnswer: "",
    explainAnswer: "",
  }},
  {{
    id: 5,
    question: "",
    options: ["", "", "", ""],
    correctAnswer: "",
    explainAnswer: "",
  }},
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

app = FastAPI(
    title="Quiz API",
    version="1.0",
    description="Quiz API"
)

add_routes(app, prompt_template | model, path = "/quiz")

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)
