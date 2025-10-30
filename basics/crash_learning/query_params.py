from fastapi import FastAPI

app = FastAPI()

books = {
  1: {"author": "J.K. Rowling", "title": "Harry Potter and the Philosopher's Stone", "category": "Fantasy"},
  2: {"author": "George Orwell", "title": "1984", "category": "Dystopian"},
  3: {"author": "Harper Lee", "title": "To Kill a Mockingbird", "category": "Classic"},
}

@app.get("/books/")
def get_books(category: str):
  books_list = []
  for i in books:
    books_list.append(books[i])
  for i in books_list:
    if i["category"]==category:
      return i        
    

@app.get("/books/{book}/")
async def get_books(book: str, category: str):
  books_list = []
  for i in books:
    books_list.append(books[i])
  for i in books_list:
    if i["category"]==category and i["author"]==book:
      return i