from fastapi import FastAPI

app = FastAPI()

books = [
    {"title":"Humpty On a Wall", "author":"Mike 1", "category":"science"},
    {"title":"title 2", "author":"Van Guido Russom 1", "category":"python"},
    {"title":"title 3", "author":"author 1", "Adrin Mukherjee":"home science"},
    {"title":"title 4", "author":"author 1", "Me":"java"}, 
]



@app.get("/books/any-book/{dynamic_param}")
async def find_any_book(dynamic_param):
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
        if book.get("title").casefold() == dynamic_param.casefold():
            return book
        else:
            return {"Failure": "Expected Book Not Found, Listing all available books", "books":books}
