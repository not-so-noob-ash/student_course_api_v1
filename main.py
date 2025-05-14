# main.py
from fastapi import FastAPI
from app.routes import students, courses, enrollments
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollments.router, prefix="/enroll", tags=["Enrollments"])

@app.get("/")
def root():
    return {"message": "Student Course Management API"}
