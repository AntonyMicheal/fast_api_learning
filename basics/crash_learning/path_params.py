from fastapi import FastAPI

app = FastAPI()
books = {
  1: {"author": "J.K. Rowling", "title": "Harry Potter and the Philosopher's Stone", "category": "Fantasy"},
  2: {"author": "George Orwell", "title": "1984", "category": "Dystopian"},
  3: {"author": "Harper Lee", "title": "To Kill a Mockingbird", "category": "Classic"},
}

@app.get("/read-all-books")
async def get_all_books():
  return books

@app.get("/read-all-books/{dynamic_books}")
def read_all_books(dynamic_books: str):
  return{"books": dynamic_books}


@app.get("/read-all-books/book1")
def read_book_1():
  return {"Book 1": "read books 1"}

@app.get("/read-book/{book}")
async def read_book(book: str):
  for i in books:
    if book == str(i):
      return books[i]
    else:
      return{"error": "book not present"}