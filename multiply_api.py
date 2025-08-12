# multiply_api.py

# Multiplication API with Validation
# Objective:
# Create a FastAPI application that exposes a POST endpoint to multiply two
# numbers and return the result. Ensure that the input is validated and 
# both a and b should be integers.
# Instructions:
# Create a FastAPI application:
# Define a POST endpoint at /multiply to accept two numbers, a and b.
# Validate that both a and b are integers using Pydantic models.
# Test the API using:
# Postman (send JSON body with a and b).
# curl to test the endpoint with JSON data.
# Python requests for programmatic testing.
# Bonus: Return an error message if the input values are not integers.


from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict

# Create an instance of the FastAPI application
app = FastAPI()

# Define a Pydantic model for the request body
class MultiplyInput(BaseModel):
    # 'a' is a required field of type integer.
    a: int
    
    # 'b' is a required field of type integer.
    b: int

# POST endpoint for multiplication with validation
@app.post("/multiply", status_code=status.HTTP_200_OK)
async def multiply_numbers(data: MultiplyInput) -> Dict[str, int]:
    """
    Multiplies two integers, 'a' and 'b', and returns the result.
    If the input values are not integers, FastAPI returns an error automatically.
    """
    try:
        # Pydantic has already validated that 'data.a' and 'data.b' are integers.
        # Perform the multiplication.
        result = data.a * data.b
        
        # Return the result as a dictionary, which FastAPI will convert to JSON.
        return {"result": result}
    except Exception as e:
        # This part handles any unexpected errors, though Pydantic handles validation errors.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An internal error occurred: {str(e)}"
        )
        
        