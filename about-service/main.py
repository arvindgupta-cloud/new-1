from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def about():
    return {"message": "This is About Service"}
