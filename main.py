from fastapi import FastAPI

app = FastAPI()

# in-memory storage of data
notes = []

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/notes")
def get_notes(notes: str):
    return {"notes": notes}

@app.post("/notes")
def create_note(title: str, content: str):
    note = {"id": len(notes) + 1, "title": title, "content": content}
    notes.append(note)
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Deleted"}
    return {"error": "Not found"}