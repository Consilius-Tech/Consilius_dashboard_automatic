from fastapi import FastAPI

app  = FastAPI( title = "Consilius BI platform")

@app.get("/")
def read_root():
    return {"Status": "Operational", "service": "Consilius BI Backend"}


#uvicorn app.main:app --reload