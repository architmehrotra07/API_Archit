# calculator.py
# Simple Calculator API 
# Objective:
# Create a FastAPI application that acts as a simple calculator and exposes
# endpoints to handle addition, subtraction, multiplication, and division.
# Instructions:
# 1.	Create a FastAPI application:
# Expose a POST method at /calculator to handle four operations: addition,
# subtraction, multiplication, and division.
# Accept two numbers and an operation type (add, subtract, multiply, divide) as JSON input.
# Return the result of the operation.
# Test the API using:
# Postman to test the calculator API.
# curl to test each operation (addition, subtraction, multiplication, and division).
# Python requests to send requests and receive responses.
# Bonus: Handle division by zero gracefully and return a custom error message.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

# Pydantic model for the request body
# This ensures the input has two floats and a valid operation type.
class CalculatorInput(BaseModel):
    num1: float
    num2: float
    # Literal ensures the operation is one of the specified strings.
    operation: Literal["add", "subtract", "multiply", "divide"]

# The POST endpoint for the calculator
@app.post("/calculator")
async def calculate(input_data: CalculatorInput):
    """
    Performs a calculation based on the input numbers and operation.
    """
    result = None

    if input_data.operation == "add":
        result = input_data.num1 + input_data.num2
    elif input_data.operation == "subtract":
        result = input_data.num1 - input_data.num2
    elif input_data.operation == "multiply":
        result = input_data.num1 * input_data.num2
    elif input_data.operation == "divide":
        # Bonus: Handle division by zero
        if input_data.num2 == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed."
            )
        result = input_data.num1 / input_data.num2

    return {"result": result}