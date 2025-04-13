from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/api/v1.0/predict")
def predict(
    num1: Optional[float] = Query(default=0.0),
    num2: Optional[float] = Query(default=0.0)
):
    total = num1 + num2
    prediction = 1 if total > 5.8 else 0
    return {
        "features": {"num1": num1, "num2": num2},
        "prediction": prediction
    }