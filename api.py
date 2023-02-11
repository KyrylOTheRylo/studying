from fastapi import FastAPI, HTTPException
import uvicorn
import random

app = FastAPI()


@app.get("/")
def get_root():
    return {"name": "LOH"}


@app.get("/get_trans/{transaction_id}")
def get_trans(transaction_id):
    return {"name": transaction_id}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=50300)
