from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/contact")
def contact():
    return {"message": "This is Contact Service"}
