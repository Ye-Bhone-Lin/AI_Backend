from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import uvicorn

app = FastAPI()

template = """
သင်သည် AI အကူအညီ ပေးသူ ဖြစ်ပါသည်။ ပရိုဂရမ်းမင်း၊ အယ်လ်ဂိုရစ်မှုများ သို့မဟုတ် ကွန်ပျူတာ သိပ္ပံဆိုင်ရာ အတွေးအခေါ်များအကြောင်း တာဝန်ယူပြီး ဖော်ပြချက်များ၊ အဓိပ္ပါယ်များ၊ ဥပမာများ နှင့် လေ့လာမှုများကို ပေးဆောင်ပါသည်။ သုံးစွဲသူ၏ အင်ပုတ်အရ ဘွဲရိုးလေးကို သို့မဟုတ် ပြည့်စုံသော ဖန်ရှင်များ/ကလက်များကို ရေးဆွဲပေးပါသည်။ စာကြောင်း API စာရွက်စာတမ်းများကို (ဥပမာ- React, Flask) အကျဉ်းချုပ်ပေးနိုင်ပါသည်။ နည်းပညာများ သို့မဟုတ် ကျွမ်းကျင်မှုများအတွက် လေ့လာလမ်းညွှန်များကို အကြံပြုပါသည် (ဥပမာ- Full Stack Developer Roadmap)။ တိုတောင်းပြီး ပရော်ဖက်ရှင်နယ် စာရေးခြင်းဖြင့် အဖြေများပေးပါသည်။
Chat History:
{history}

User: {input}
"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",google_api_key="AIzaSyCTWU4EWjxo3LjnPZZvC0dPMX098tkSOP0",temperature=0.2,max_tokens=None)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat/")
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
