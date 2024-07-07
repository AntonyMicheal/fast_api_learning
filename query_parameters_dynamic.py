from fastapi import FastAPI

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike", "category":"science"},
    {"title":"pinky po", "author":"Van Guido Russom", "category":"Maths"},
    {"title":"Harry potter", "author":"Rowling", "category":"home science"},
    {"title":"House Dragon", "author":"antony", "category":"science"}, 
]

#endpoint using a single query param
@app.get("/books/")
async def read_query_book(category:str):
    works = []
    for book in books:
        if book.get("category").casefold() == category.casefold():
            works.append(book)
    return works

# endpoint using multiple parameters
@app.get("/books/auth_category")
async def author_category(author:str, category:str):
    works = []
    for book in books:
        if book.get("author").casefold() == author.casefold() or book.get("category").casefold()==category.casefold():
            works.append(book)
    if len(works)>0:
        return works
    else:
        return {"failure": "No books found with the two filters"}
       
#endpoint using query param and path param(dynamic)
@app.get("/books/{title}/")
async def read_books_query_params(title:str, category:str):
    works = []
    for book in books:
        if book.get("title").casefold() == title.casefold() or book.get("category").casefold()==category.casefold():
            works.append(book)
    if len(works)>0:
        return works
    else:
        return {"failure": "No books found with the two filters"}
    
