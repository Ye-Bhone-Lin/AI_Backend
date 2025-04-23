from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from fastapi import FastAPI
import uvicorn
from langserve import add_routes

load_dotenv()
model = ChatGroq(model_name="meta-llama/llama-4-scout-17b-16e-instruct")


system_prompt1 = """
based on the user level and programming languages, please provide 5 quizs. 
{{level_programming_languages}}.
"""

prompt_template1 = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt1),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{level_programming_languages}")
    ]
)

system_prompt2 = """
Give answers.
"""

prompt_template2 = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt2),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ]
)

runnable1 = prompt_template1 | model | StrOutputParser()
runnable2 = prompt_template2 | model | StrOutputParser()

#context_chain = (
#    {
#        "question": RunnablePassthrough(),
#    }
#    | prompt_template1
#    | model
#    | StrOutputParser()
#)

#re_do_chain = (
#    {
#        "answer_from_context": context_chain,
#        "question": RunnablePassthrough()
#    }
#    | prompt_template2
#   | model
#   | StrOutputParser()
#)



app = FastAPI(
    title="Quiz API",
    version="1.0",
    description="Quiz API"
)

add_routes(app, runnable1, path="/generate-quiz")
add_routes(app, runnable2, path="/answer-quiz")
if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)
