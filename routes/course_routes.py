from fastapi import APIRouter, HTTPException
from schemas.course import CourseCreate, Course
from services import course_service, user_service, enrollment_service

router = APIRouter()

@router.post("/", response_model=Course)
def create_course(course: CourseCreate):
    return course_service.create_course(course)

@router.get("/", response_model=list[Course])
def get_courses():
    return course_service.get_all_courses()

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: int, course: CourseCreate):
    updated = course_service.update_course(course_id, course)
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated

@router.delete("/{course_id}")
def delete_course(course_id: int):
    course_service.delete_course(course_id)
    return {"message": "Course deleted"}

@router.put("/{course_id}/close", response_model=Course)
def close_enrollment(course_id: int):
    course = course_service.close_enrollment(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/{course_id}/users", response_model=list)
def get_enrolled_users(course_id: int):
    return course_service.get_users_enrolled(course_id, enrollment_service.enrollments, user_service.users)