from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def shop():
    return {"message": "Welcome to Shop Service"}
