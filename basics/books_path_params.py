from fastapi import FastAPI

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike 1", "category":"science"},
    {"title":"pinky", "author":"Van Guido Russom 1", "category":"python"},
    {"title":"title Three", "author":"author 1", "category":"home science"},
    {"title":"title 4", "author":"author 1", "Me":"java"}, 
]



@app.get("/books/{dynamic_parameter}")
async def find_any_book(dynamic_parameter: str):
    """How the Logic is working
    ----------------------------------

    We are taking in a dynamic parameter through the decorator app.get which will act like a search parameter

    - then we are looping through the books list to check for the book title that will be entered as the dynamic parameter.
     
         we are using casesfold to make it all small letter 
        and returns a new string, we can also use the lower()

        then we are checking to see  if the book name and dynamic param's equal.

        note:  make sure that you are passing the dynamic parameter name to the async function name 

    """
    for book in books:
        if book.get("title").casefold() == dynamic_parameter.casefold():
            return book
    else:
        return {"reason":"failed to fetch the book, check if you have entered the name correctly?!", "listing books that are available": books}
    
# update the code with multiple dynamic prameters

@app.get("/books/multiple-filter/{title}/wrote/{author}")
async def read_author_book(title:str, author:str):
    for book in books:
        if book.get("title").casefold() == title.casefold() and book.get("author").casefold() == author.casefold():
            return book 
        
    else:
        return {"reason":"failed to fetch the book, check if you have entered the name correctly?!", "listing books that are available": books}