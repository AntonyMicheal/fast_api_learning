from fastapi import FastAPI

app = FastAPI()

@app.get("/first-endpoint")
async def first_endpoint():
    return {"message":"Hello World"}

books = [
    {"title":"title 1", "author":"Mike 1", "category":"science"},
    {"title":"title 2", "author":"Van Guido Russom 1", "category":"python"},
    {"title":"title 3", "author":"author 1", "Adrin Mukherjee":"home science"},
    {"title":"title 4", "author":"author 1", "Me":"java"}, 
]


# Write an API endpoint for exploring dynamic parameters

@app.get("/books")
async def read_all_books():
    return books

#to make sure that it returns a specific data type - we can specify the data type. like int or str
@app.get("/books/{dynamic_parameter}")
async def read_books(dynamic_parameter: str):
    for book in books:
        if book.get("title").casefold() == dynamic_parameter.casefold():
            return book
