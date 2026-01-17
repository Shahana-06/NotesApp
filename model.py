from pydantic import BaseModel, Field
from typing import Optional

class NoteBase(BaseModel):
    """Base model for notes"""
    note_name: str = Field(..., min_length=1, max_length=200, description="Title of the note")
    note_content: str = Field(..., description="Content of the note")

class NoteCreate(NoteBase):
    """Model for creating a new note"""
    pass

class NoteUpdate(BaseModel):
    """Model for updating a note (all fields optional)"""
    note_name: Optional[str] = Field(None, min_length=1, max_length=200)
    note_content: Optional[str] = None

class Notes(NoteBase):
    """Model for returning notes (includes ID)"""
    note_id: int
    
    class Config:
        from_attributes = True  # Allows reading from ORM models
