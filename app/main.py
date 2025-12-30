from fastapi import FastAPI

app = FastAPI(title="Technical Test - FastAPI")

@app.get("/")
def health_check():
    return {"status": "ok"}