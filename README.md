

# Student Course Management API
Project made by Ashwani Kumar Email:(ashwani1508kumar@gmail.come) as a task by Novelti Solution for intern Python Developer postion.
This is a minimal REST API for managing students and their course enrollments using FastAPI, SQLAlchemy, and PostgreSQL (used sqlite for testing).

## Features

- Create students and courses
- Enroll students into courses
- Fetch student details with enrolled courses
- Fetch course details with enrolled students
- Email validation
- Pagination support (optional limit/offset)
- Basic unit tests

## Technologies Used

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL / SQLite
- pytest

## Setup Instructions

```bash
# Clone or extract the project
cd student_course_api

# (Optional) Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

## Sample curl Commands

```bash
# Create a student
curl -X POST http://localhost:8000/students/ -H "Content-Type: application/json" -d '{"name": "Ash", "email": "ash@example.com"}'

# Create a course
curl -X POST http://localhost:8000/courses/ -H "Content-Type: application/json" -d '{"title": "Math 101", "description": "Basic Math by T1"}'

# Enroll student
curl -X POST http://localhost:8000/enroll/ -H "Content-Type: application/json" -d '{"student_id": 1, "course_id": 1}'

# Get student
curl http://localhost:8000/students/1

# Get course
curl http://localhost:8000/courses/1
```

## Run Tests

```
pytest
```
