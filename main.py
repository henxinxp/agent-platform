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