from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def contact():
    return {"message": "Contact us at support@example.com"}
