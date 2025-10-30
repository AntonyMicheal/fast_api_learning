from fastapi import FastAPI

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike", "category":"science"},
    {"title":"pinky po", "author":"Van Guido Russom", "category":"Maths"},
    {"title":"Harry potter", "author":"Rowling", "category":"home science"},
    {"title":"House Dragon", "author":"antony", "category":"science"} 
]

@app.delete("/books/{book_title}")
async def delete_books(book_title: str):
  for i in books:
    if i["title"]==book_title:
      books.remove(i)
      break

@app.get("/books/read_all")
async def read_all():
  return books