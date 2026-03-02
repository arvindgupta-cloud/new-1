from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/home")
def home():
    return {"message": "Welcome to Home Service"}
