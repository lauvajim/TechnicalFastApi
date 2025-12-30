from fastapi import FastAPI

app = FastAPI(title="Technical Test - FastAPI")

@app.get("/prueba")
def health_check():
    return {"status": "ok"}