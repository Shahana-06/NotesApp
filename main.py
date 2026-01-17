from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from config import session, engine 
from model import Notes, NoteCreate, NoteUpdate
from sqlalchemy.orm import Session
import db_model

app = FastAPI(title="Notes API", version="1.0.0")

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
db_model.Base.metadata.create_all(bind=engine)

# Initial sample data
initial_notes = [
    Notes(
        note_id=1, 
        note_name="To do list", 
        note_content="1. Update Github\n2. Update Resume\n3. Brush up concepts\n4. Call Parents"
    ), 
    Notes(
        note_id=2, 
        note_name="Things to pack", 
        note_content="1. Laptop, charger\n2. Visa, Passport\n3. Offer Letter"
    ),
]

# Database dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# Initialize database with sample data
def init_db():
    db = session()
    try:
        count = db.query(db_model.Notes).count()  # Fixed: Added parentheses
        if count == 0:
            for note in initial_notes:
                db.add(db_model.Notes(**note.model_dump()))
            db.commit()
    finally:
        db.close()

init_db()

@app.get("/")
def home():
    return {
        "message": "Notes API",
        "version": "1.0.0",
        "endpoints": {
            "GET /notes": "Get all notes",
            "GET /notes/{id}": "Get note by ID",
            "POST /notes": "Create a new note",
            "PUT /notes/{id}": "Update a note",
            "DELETE /notes/{id}": "Delete a note"
        }
    }

@app.get("/notes", response_model=list[Notes])
def get_notes(db: Session = Depends(get_db)):
    """Get all notes"""
    db_notes = db.query(db_model.Notes).all()
    return db_notes

@app.get("/notes/{note_id}", response_model=Notes)
def get_note_by_id(note_id: int, db: Session = Depends(get_db)):
    """Get a specific note by ID"""
    db_note = db.query(db_model.Notes).filter(
        db_model.Notes.note_id == note_id
    ).first()
    
    if not db_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    return db_note

@app.post("/notes", response_model=Notes, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    """Create a new note"""
    # Get the next available ID
    max_id = db.query(db_model.Notes).count()
    
    # Create new note with database model
    db_note = db_model.Notes(
        note_id=max_id + 1,
        note_name=note.note_name,
        note_content=note.note_content
    )
    
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    
    return db_note

@app.put("/notes/{note_id}", response_model=Notes)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    """Update an existing note"""
    db_note = db.query(db_model.Notes).filter(
        db_model.Notes.note_id == note_id
    ).first()
    
    if not db_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    # Update only provided fields
    if note.note_name is not None:
        db_note.note_name = note.note_name
    if note.note_content is not None:
        db_note.note_content = note.note_content
    
    db.commit()
    db.refresh(db_note)
    
    return db_note

@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    """Delete a note"""
    db_note = db.query(db_model.Notes).filter(
        db_model.Notes.note_id == note_id
    ).first()
    
    if not db_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    
    db.delete(db_note)
    db.commit()
    
    return None