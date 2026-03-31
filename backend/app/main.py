from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from .database import SessionLocal, engine

app = FastAPI(title="Consilius BI Platform")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/healthcheck")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "Integration Operational", "database": "Connected"}
    except Exception as e:
        return {"status": "Integration Failed", "error": str(e)}

#uvicorn app.main:app --reload