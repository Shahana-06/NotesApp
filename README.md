# Notes API - FastAPI Backend

A RESTful API for managing notes built with FastAPI and PostgreSQL.

## Features

- ✅ Create, Read, Update, Delete (CRUD) operations for notes
- ✅ PostgreSQL database integration
- ✅ Input validation with Pydantic
- ✅ CORS enabled for frontend integration
- ✅ Proper error handling and HTTP status codes
- ✅ Auto-generated API documentation

## Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## Installation

1. **Clone the repository** (or create project directory)
   ```bash
   mkdir notes-api
   cd notes-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   - Create a PostgreSQL database named `shahanas` (or your preferred name)
   - Copy `.env.example` to `.env` and update with your credentials:
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` with your database credentials

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

### Get All Notes
```http
GET /notes
```

### Get Note by ID
```http
GET /notes/{note_id}
```

### Create Note
```http
POST /notes
Content-Type: application/json

{
  "note_name": "My Note",
  "note_content": "Note content here"
}
```

### Update Note
```http
PUT /notes/{note_id}
Content-Type: application/json

{
  "note_name": "Updated Title",
  "note_content": "Updated content"
}
```

### Delete Note
```http
DELETE /notes/{note_id}
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
notes-api/
├── main.py           # FastAPI application and routes
├── model.py          # Pydantic models for validation
├── db_model.py       # SQLAlchemy ORM models
├── config.py         # Database configuration
├── requirements.txt  # Python dependencies
├── .env             # Environment variables (create from .env.example)
└── .env.example     # Example environment variables
```

## Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Database Schema

**Notes Table**
- `note_id` (Integer, Primary Key)
- `note_name` (String)
- `note_content` (String)

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK` - Successful GET, PUT requests
- `201 Created` - Successful POST request
- `204 No Content` - Successful DELETE request
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation error

## Security Notes

⚠️ **For Production:**
- Store database credentials securely (use environment variables)
- Update CORS settings to allow only your frontend domain
- Use HTTPS
- Implement authentication/authorization
- Add rate limiting
- Use connection pooling (already configured)

## Testing

You can test the API using:
- Swagger UI at `/docs`
- curl commands
- Postman
- Python requests library

Example curl command:
```bash
curl -X POST "http://localhost:8000/notes" \
  -H "Content-Type: application/json" \
  -d '{"note_name":"Test Note","note_content":"This is a test"}'
```

## License

MIT
