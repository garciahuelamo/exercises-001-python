from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    publication : int

books = []

@app.post('/api/books', status_code=201)
def validation_books(book: Book):
    if any (u['book'] == book.title for u in books):
        raise HTTPException(status_code=400, detail = "This book is already saved")
    
    new_book = {
        "id": len(books) + 1,
        "title" : book.title,
        "author" : book.author,
        "publication" : book.publication
    }

    books.append(new_book)

    return {"message": "Book created", "Book" : new_book}

@app.route('/api/books')
def list_books():
    return {"Books" : books}


    
