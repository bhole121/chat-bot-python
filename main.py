from fastapi import FastAPI
import uvicorn
from app import models
from app.db import engine
from app.routes import router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World 2"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)