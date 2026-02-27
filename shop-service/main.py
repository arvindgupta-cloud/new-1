from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/shop")
def shop():
    return {"message": "This is Shop Service"}
