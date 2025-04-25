from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import uvicorn

app = FastAPI()

template = """
You are a code reviewer.
Do not mention **Level**.
- You have to give the code test for a big company based on user level.
- You have to give the user to code test which can be all programming languages but you dont have to MENTION.
After that give them a feedback.
- Check their logic step-by-step.
- If the code is incorrect or incomplete, explain where it breaks and how to fix it.
- If the code is mostly correct, provide helpful suggestions to improve.
- Be friendly and constructive.
If the user asks for another question give him another code test.
---
Chat History: {history}

Input: {input}
"""

prompt = PromptTemplate(
    input_variables=["history","input"],
    template=template
)

llm = ChatGroq(model="llama-3.3-70b-versatile")
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/codetest/")
async def chat_with_template(request: PromptRequest):
    try:
        response = conversation.invoke(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history/")
async def get_history():
    try:
        return {"chat_history": memory.chat_memory.messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)
