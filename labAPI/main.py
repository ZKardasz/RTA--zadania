from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/api/v1.0/predict")
def predict(
    num1: Optional[float] = Query(default=None),
    num2: Optional[float] = Query(default=None)
):
    # Jeśli numery nie zostały podane lub są None, ustaw domyślnie 0.0:
    if num1 is None:
        num1 = 0.0
    if num2 is None:
        num2 = 0.0
        
    total = num1 + num2
    prediction = 1 if total > 5.8 else 0
    return {
        "features": {"num1": num1, "num2": num2},
        "prediction": prediction
    }