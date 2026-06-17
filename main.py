from fastapi import FastAPI

from app.api.chat import router as chat_router


app = FastAPI(
    title="Agent Platform"
)

app.include_router(
    chat_router
)



"""
from fastapi import FastAPI

from app.api.chat import router

app = FastAPI()

app.include_router(router)




from fastapi import FastAPI

from simple_agent import ask

app = FastAPI()

@app.get("/")
def root():

    return {
        "message":"Agent Platform Running"
    }

@app.get("/ask")
def ask_agent(question:str):

    answer = ask(question)

    return {
        "question":question,
        "answer":answer
    }

"""