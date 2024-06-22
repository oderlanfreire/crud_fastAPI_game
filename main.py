from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def gamestart():
    return "Bem vindo ao Game API"


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)