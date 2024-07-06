# fast_api_learning
learning fast api from scratch..


## virtual environment.

___

A virtual environment is a python environment which is isolated from those in other python environments.

## How to Install Dependencies.

* pip is the python package manager.
* its used to install and update packages.
* try to use the most recent pip.

- install the following two packages 
    - fastapi 
    - uvicorn[standard]
  
you can use pip list to see all the packages that have been installed using pip.
also you can use ```pip install -r requirements.txt``` to install all the dependencies from requirements.txt file.

### GET HTTP Request method
___ 

- create a new file books.y
- import fastapi 
    ```Python
    from fastapi import FastAPI
    ```

- Now instantiate that object by - 
    ```Python
    app = FastAPI()
    ```

- Now that you have created the object we need to create a function that will return us a value (ie - so that the client can use / consume the API.)

    - To do that you can follow the following steps
    ```Python
    async def first_api():
        return {"message":"hello World!!"}
    ```

***NOTE***: We dont need to specifically mention `async` keyword before the function because in case of fast api it will do that behind the scenes. although its a good practice to keep the `async` keyword.

- Now to access the function as an API end point we need to specify that using a decorator right before our function
the decorator will look like this -
    ```Python
    @app.get("/endpoint-name")
    ```

example: 

```Python   
from fastapi import FastAPI

app = FastAPI()

@app.get("/route-endpoint")
async def read_route():
    return {"message":"Hello World!!"}
 ```

 - now to run the API you need to execute the following command in the terminal

    ```python
        uvicorn books:app --reload
    ```

This will start the server..


# Swagger UI

- Once your API starts running in the local you can remove the endpoint name and add `docs` right after the port nummber to access the swagger UI
    - Example: `http://127.0.0.1:8000/docs#/`

You can see all the endpoints that are currently part of your fast api application eg -  books.py - apis

- Status codes
    - 200 means all OK


## Path Parameters

- request parameters that are attached to the URL.
- usually defined as a way to find information based on location
- 
    ```Python   
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/route-endpoint")
    async def read_route():
        return {"message":"Hello World!!"}
    ```
In the above example you can see that the path thats specified in the app.get is actual path in which we are getting the API.

