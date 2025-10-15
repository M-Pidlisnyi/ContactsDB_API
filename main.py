from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from . import db_scripts as db

app = FastAPI()

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    description: str


@app.get("/")
def index():
    return "Hello, World!"

@app.get("/contacts/all")
def get_all_contacts():
    return db.get_all_contacts()

@app.get("/contacts/{contact_id}", response_model=Contact)
def get_contact(contact_id: int):
    row = db.get_contact_by_id(contact_id)
    if not row:
        return HTTPException(status_code=404, detail="Contact not found")
    return Contact(id=row[0], first_name=row[1], last_name=row[2], email=row[3], description=row[4])