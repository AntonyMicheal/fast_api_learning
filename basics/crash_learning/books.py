
"""API books"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint") # exposing endpoint, usage of decorator
async def first_api():
  """first API"""
  return{"Message": "Hello World, It's my first API"}

@app.get("/api-endpoint/book2")
async def book_2():
  """first API"""
  return {"Book_2": "Harry Poter and the 40 thieves"}

books = {
  1: {"author": "J.K. Rowling", "title": "Harry Potter and the Philosopher's Stone", "category": "Fantasy"},
  2: {"author": "George Orwell", "title": "1984", "category": "Dystopian"},
  3: {"author": "Harper Lee", "title": "To Kill a Mockingbird", "category": "Classic"},
}

@app.get("/get-books")
async def get_books():
  """books api"""
  return books
