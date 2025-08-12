# pip install fastapi install this in terminal
# pip install uvicorn install this in terminal 

# from pydantic import BaseModel lets you create a data structure that makes sure
# the information your API receives is in the correct format.
# It's like a blueprint or a checklist for the data, 
# ensuring that a field named 'a' is always an integer and a field named 'b' is also an integer.
# This prevents errors by catching incorrect data types before your code tries to process them.

from fastapi import FastAPI
from pydantic import BaseModel

## Create one object of fast api i.e variable
app = FastAPI()

# The line @app.get("/Archit/Mehrotra/xyz") is a decorator in FastAPI.
# It tells your web app to run the function below it
# whenever someone visits the exact URL /Archit/Mehrotra/xyz.
# It's a rule that connects a specific web address to a piece of your Python code.

@app.get("/Archit/Mehrotra/xyz")

#create add function and pass values a and b with type integer

def add(a:int,b:int):
    return a+b

# Type below command in terminal to start Uvicorn server
#            uvicorn test:app --reload
# test.py is my file name so used filename test after uvicorn
# Look for the FastAPI application named 'app' inside the file 'test.py.'
# --reload: Automatically restart the server whenever you save changes to your code. 
# This is a huge time-saver for development.
# when we hit the enter then its given Uvicorn is running on http://127.0.0.1:8000.
# http://127.0.0.1 this is IP address and 8000 is port number of my local system. 
# copy the URL and past on browser you will click on the check box. 
# After url put /docs and you will see Fast API swagger UI page opening.


# This line creates a new data model named subtractmodel. 
# It inherits from BaseModel from Pydantic, which gives it the power to validate data.

class subtractmodel(BaseModel):
    a: int
    b: int

#  Python function definition  subtract and it takes two arguments, a and b, 
#  which are both expected to be integers.

def subtract(a:int,b:int):
    return a-b

# This is a FastAPI decorator that tells your application to use the 
# function below it whenever a POST request is sent to the /subtract URL.

@app.post("/subtract")

# This defines the function that handles the POST request. 
# It takes a single argument, model, which is an instance of the subtractmodel class. 
# FastAPI uses Pydantic to automatically read the request body and validate
# that the data matches the a and b integer fields you defined.

def subtract_numbers(model: subtractmodel):
    return subtract(model.a, model.b)

print(add(3,4))

