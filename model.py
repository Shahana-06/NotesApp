from pydantic import BaseModel

class Notes (BaseModel):
    note_id : int
    note_name : str
    note_content : str