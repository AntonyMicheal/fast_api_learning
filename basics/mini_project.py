"""This is a mini project of FastAPI"""
from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike", "category":"science"},
    {"title":"pinky po", "author":"Van Guido Russom", "category":"Maths"},
    {"title":"Harry potter", "author":"Rowling", "category":"home science"},
    {"title":"House Dragon", "author":"antony", "category":"science"} 
]

@app.get("/books/read_all")
async def read_all_books():
  """reading all books"""
  return books

@app.get("/books/read_books")
async def read_books_by_category(category: str):
  """reading books by category using query parameter"""
  books_list = []
  for i in books:
    if i["category"]==category:
      books_list.append(i)
  if len(books_list) > 0:
    return books_list
  else:
    return {"Error":"Category not present"}

@app.get("/books/read_books/{title}")
async def ready_boks_by_path(title: str):
  """reading books by title using category"""
  for i in books:
    if i["title"]==title:
      return i
  return {"error": "book not found"}

@app.post("/books/create_books/")
async def create_books(new_book: dict = Body()):
    """creating new books"""
    books.append(new_book)
    return {"message": "book created", "book": new_book}
  

@app.put("/books/update_book/")
async def update_book(title: str, updated_book = Body()):
  """Update books by title using query param"""
  for i in books:
    if i["title"] == title:
      books.remove(i)
      books.append(updated_book)
      break

@app.put("/books/update_book/{category}")
async def update_books(category: str, updated_book = Body()):
  """Update books by title using query param"""
  for i in books:
    if i["category"] == category:
      books.remove(i)
      books.append(updated_book)
      break

@app.delete("/books/delete_book/")
async def delete_book(category):
  """delete book based on category"""
  for i in books:
    if i["category"]==category:
      books.remove(i)
  return None