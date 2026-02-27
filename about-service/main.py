from fastapi import FastAPI

app = FastAPI()

# GCE health check route
@app.get("/")
def health():
    return {"status": "ok"}

# Actual service route
@app.get("/about")
def about():
    return {"message": "This is About Service"}
