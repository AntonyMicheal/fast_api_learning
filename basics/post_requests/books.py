from fastapi import Body, FastAPI

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike", "category":"science"},
    {"title":"pinky po", "author":"Van Guido Russom", "category":"Maths"},
    {"title":"Harry potter", "author":"Rowling", "category":"home science"},
    {"title":"House Dragon", "author":"antony", "category":"science"}, 
]

# sample get request - just for reference

@app.get("/books/")
async def read_query_book(category:str):
    works = []
    for book in books:
        if book.get("category").casefold() == category.casefold():
            works.append(book)
    return works

@app.post("/books/create-book")
async def create_books(new_book = Body()):
    books.append(new_book)