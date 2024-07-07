# fast_api_learning
learning fast api from scratch..


## virtual environment.

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

In FastAPI, path parameters are used to capture values from the URL path of an incoming request. They allow you to define parts of the URL that contain variables, which can then be used as input parameters to your FastAPI route functions.

### Defining Path Parameters

To define a path parameter in FastAPI, you include a variable enclosed in curly braces `{}` within the route path string. For example, consider a route that retrieves information about a specific user identified by their `user_id`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}
```

In this example:
- `/users/{user_id}` defines a path parameter named `user_id`.
- `user_id: int` in the function parameters declares `user_id` as a parameter of type `int`. FastAPI automatically converts the captured path segment to the specified type (`int` in this case).

### Using Path Parameters

When a request is made to `/users/123`, FastAPI captures `123` as the value of `user_id` and passes it to the `get_user` function. The function can then use this value (`123` in this case) to retrieve and return data specific to that user.

### Multiple Path Parameters

You can have multiple path parameters in a single route:

```python
@app.get("/users/{user_id}/items/{item_id}")
async def get_item(user_id: int, item_id: str):
    return {"user_id": user_id, "item_id": item_id}
```

In this example, `/users/{user_id}/items/{item_id}` captures both `user_id` and `item_id` from the URL path.

### Path Parameter Types

FastAPI supports different types for path parameters, such as `int`, `float`, `str`, `uuid`, etc. It also allows you to specify optional parameters using Python's Optional type or default values.

### Dynamically Adding Path Parameters

Path parameters are added dynamically by defining routes with `{}` placeholders for the variable parts of the URL path. As long as the route patterns match the incoming request paths, FastAPI will appropriately capture and pass the values to your route functions.

### Summary

Path parameters in FastAPI are a powerful feature for building RESTful APIs, allowing you to define dynamic parts of URLs and capture them as input parameters in your route functions. They provide a straightforward way to handle variable data within your API paths.

In FastAPI, the order in which you define your endpoint functions can matter due to how route matching works in Python's ASGI (Asynchronous Server Gateway Interface) application. Here are the key reasons why function order can be important:

## Order in FastAPI functions
1. **Route Matching Order**: FastAPI matches incoming requests to the appropriate endpoint function based on the order of route definitions. When a request arrives, FastAPI checks the defined routes sequentially from top to bottom until it finds a route that matches the request's URL path and HTTP method. 

   - If you have a more specific route defined before a more general one, the more specific route will be matched first. For example:
     ```python
     @app.get("/users/{user_id}")
     async def get_user(user_id: int):
         ...

     @app.get("/users/me")
     async def get_current_user():
         ...
     ```
     Here, requests to `/users/me` will match the `get_current_user` function because it's defined before `/users/{user_id}`. If you reverse the order, `/users/{user_id}` would match any request that starts with `/users/`, potentially overriding the more specific `/users/me` route.

2. **Method Matching**: FastAPI distinguishes between different HTTP methods (GET, POST, PUT, DELETE, etc.) when matching routes. If you define two routes with the same path but different HTTP methods, they are considered distinct endpoints.

   - For example:
     ```python
     @app.get("/items/{item_id}")
     async def read_item(item_id: int):
         ...

     @app.put("/items/{item_id}")
     async def update_item(item_id: int, updated_item: Item):
         ...
     ```
     Here, a `GET` request to `/items/{item_id}` will match the `read_item` function, while a `PUT` request to the same path will match the `update_item` function.

3. **Fallback Routes**: FastAPI allows you to define a "catch-all" or fallback route using `/{path:path}`, which matches any path. This should typically be defined last to ensure that more specific routes are checked first.

   - Example:
     ```python
     @app.get("/users/{user_id}")
     async def get_user(user_id: int):
         ...

     @app.get("/{path:path}")
     async def catch_all(path: str):
         ...
     ```
     Here, `/users/{user_id}` will be matched before the catch-all route `/{path:path}`.

### Importance of Order

The order of defining functions in FastAPI determines which function will handle a specific request based on its URL path and HTTP method. Therefore, organizing your endpoint functions in a logical order ensures that requests are routed correctly and efficiently. Misordering can lead to unexpected behavior where requests might not be handled as intended or might not match the expected route handlers.