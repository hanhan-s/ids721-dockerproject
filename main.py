from fastapi import FastAPI
import uvicorn
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Duke"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}
    
@app.get("/api/bmicalculator/")
async def bmicalculator(height: float, weight: float, age: Optional[int] = None):

    if age is None:
        age = 0

    bmi = round(weight / (height * height), 2)
    if bmi < 18.5:
        return JSONResponse(
            content={
                "result": "Underweight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age
            },
            status_code=200)
    elif bmi >= 18.5 and bmi < 24.9:
        return JSONResponse(
            content={
                "result": "Normal weight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
    elif bmi >= 25.0 and bmi < 29.9:
        return JSONResponse(
            content={
                "result": "Overweight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
    elif bmi >= 30.0 and bmi < 39.9:
        return JSONResponse(
            content={
                "result": "Obese",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
    elif bmi >= 40.0:
        return JSONResponse(
            content={
                "result": "Morbidly Obese",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')