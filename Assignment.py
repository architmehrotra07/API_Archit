# User Registration API
# Objective:
# Create a FastAPI application that exposes a POST endpoint to register a user. 
# The API should accept a JSON body with a username, email, and password. 
# The application should validate the input, ensuring the email is in the correct 
# format and the password has at least 8 characters.
# Instructions:
# Create a FastAPI application:
# Define a POST method at /register to accept the user's username, email, 
# and password in JSON format.
# Use Pydantic validation to ensure the email is a valid email format and
# the password has a minimum length of 8 characters.
# Return a success message if registration is successful.
# Test the API using:
# Postman to register a new user.
# curl to test the registration endpoint with valid and invalid data.
# Python requests to test user registration programmatically.
# Bonus: Store the registered users in memory (for the sake of the assignment)
# and return the list of registered users when requested.

# Import necessary libraries from FastAPI and Pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from typing import List
                                                                                                                                                                                                                                                                                                                                                                                                                                         
# Initialize the FastAPI application 
app = FastAPI()

# ----------------------------------------------------------------------------- 
# We'll use a list to store dictionaries representing user data.
registered_users = []

class UserRegistration(BaseModel):
    # Field validation:
    # username is a string.
    # EmailStr provides built-in email format validation.
    # The password field has a minimum 8 length constraint.
    
    username: str
    email: EmailStr
    password: str = Field(..., min_length=8)  # '...' means the field is required.

# Pydantic model to represent the user data we store (without the password).
class UserInDB(BaseModel):
    username: str
    email: EmailStr

# -----------------------------------------------------------------------------
# API Endpoints

# POST endpoint for user registration
@app.post("/register")
async def register_user(user: UserRegistration):
    
 
    """
async def: Makes the function run efficiently by not blocking other tasks 
while it waits for things like database operations.

register_user: This is the function's name.

(user: UserRegistration): This tells FastAPI to automatically check
if the incoming data matches the required username, email, and password fields 
defined in your UserRegistration model. It handles validation for you.
    """
    
    # Check if a user with the same email already exists (simple check for this example)
    for existing_user in registered_users:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    # If all validations pass and the email is unique, "register" the user.
    # For this example, we just add the user's data to our in-memory list.
    # In a real-world scenario, you would hash the password and save it to a database.
   
    user_data = user.model_dump()
    registered_users.append(user_data)
    
    # Return a success message
    return {"message": "User registered successfully!"}

# Bonus Endpoint: GET endpoint to retrieve all registered users

@app.get("/users", response_model=List[UserInDB])
async def get_all_users():
    
    """
    Returns a list of all registered users (excluding their passwords).
    """
    # Create a list of UserInDB models from the stored data to exclude passwords.
    return [UserInDB(username=user["username"], email=user["email"]) for user in registered_users]