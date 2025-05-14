from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


# Student Schemas
class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int

    class Config:
        from_attributes = True

class StudentOutWithCourses(StudentOut):
    courses: List[str] = []



# Course Schemas
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int

    class Config:
        from_attributes = True

class CourseOutWithStudents(CourseOut):
    students: List[str] = []



# Enrollment
class EnrollmentRequest(BaseModel):
    student_id: int
    course_id: int
