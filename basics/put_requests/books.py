from fastapi import Body, FastAPI

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike", "category":"science"},
    {"title":"pinky po", "author":"Van Guido Russom", "category":"Maths"},
    {"title":"Harry potter", "author":"Rowling", "category":"home science"},
    {"title":"House Dragon", "author":"antony", "category":"science"} 
]

# sample get request - just for reference

@app.get("/books/")
async def read_query_book(category:str):
    works = []
    for book in books:
        if book.get("category").casefold() == category.casefold():
            works.append(book)
    return works

@app.put("/books/update_books")
async def update_books(update_book = Body()):
    for i in range(len(books)):
        if books[i].get("title").casefold() == update_book.get("title").casefold():
            books[i] = update_book
    return books