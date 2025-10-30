from fastapi import Body, FastAPI

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike", "category":"science"},
    {"title":"pinky po", "author":"Van Guido Russom", "category":"Maths"},
    {"title":"Harry potter", "author":"Rowling", "category":"home science"},
    {"title":"House Dragon", "author":"antony", "category":"science"}
]

# sample get request - just for reference

@app.post("/books/create_book")
async def create_book(new_book=Body()):
  books.append(new_book)

@app.get("/books/{get_author}/")
async def get_books(get_author: str, category: str):
  for i in books:
    if i["author"]==get_author and i["category"]==category:
      return i
    else:
      return {"Error": "Author / Category Missmatch"}

@app.get("/books/read_all")
async def read_books():
  return books

