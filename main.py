from fastapi import FastAPI, Depends
from config import session, engine 
from model import Notes
from sqlalchemy.orm import Session
import db_model

app = FastAPI()

#To create table
db_model.Base.metadata.create_all(bind = engine)

notes = [
    Notes (note_id = 1, note_name="To do list", note_content="1. Update Github\n2. Update Resume\n3. Brush up concepts\n4. Call Parents"), 
    Notes (note_id = 2, note_name= "Things to pack", note_content="1. Laptop, charger\n2. Visa, Passport\n3. Offer Letter"),
]

#To start and end the session automatically, once
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db ():
    db = session()

    #To ensure same data is added only once
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
def get_notes(db: Session = Depends (get_db)):
#db dependency (on get_db) is injected using Depends from fast_api
    db_notes = db.query(db_model.Notes).all()
    return db_notes

@app.get("/notes/{id}")
def get_notes_by_id (id: int, db: Session = Depends (get_db)):
    db_note = db.query(db_model.Notes). filter(db_model.Notes.note_id == id).first()
    return db_note

@app.post("/notes")
def create_note(title: str, content: str):
    note = Notes(note_id= len(notes) + 1, note_name= title, note_content= content)
    notes.append(note)
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Deleted"}
    return {"error": "Not found"}