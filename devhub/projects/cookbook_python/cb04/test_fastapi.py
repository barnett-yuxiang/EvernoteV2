from fastapi import FastAPI
from datetime import date


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/current-date")
async def current_date():
    return {"date:": date.today().isoformat()}
