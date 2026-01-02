from fastapi import FastAPI
from config import session, engine 
from model import Notes
import db_model

app = FastAPI()

#To create table
db_model.Base.metadata.create_all(bind = engine)

notes = [
    Notes (note_id = 1, note_name="To do list", note_content="1. Update Github\n2. Update Resume\n3. Brush up concepts\n4. Call Parents"), 
    Notes (note_id = 2, note_name= "Things to pack", note_content="1. Laptop, charger\n2. Visa, Passport\n3. Offer Letter"),
]

def init_db ():
    db = session()

    count = db.query (db_model.Notes).count

    if count==0:
        for note in notes:
            db.add(db_model.Notes(**note.model_dump()))

    db.commit()

init_db()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/notes")
def get_notes():
    # db = session ()
    return notes

@app.post("/notes")
def create_note(title: str, content: str):
    note = Notes(note_id= len(notes) + 1, note_name= title, note_content= content)
    # notes.append(note)
    db.add(db_model.Notes(**note.model_dump()))
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Deleted"}
    return {"error": "Not found"}