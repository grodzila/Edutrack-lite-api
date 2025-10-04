from fastapi import APIRouter, HTTPException
from schemas.enrollment import EnrollmentCreate, Enrollment
from services import enrollment_service, user_service, course_service

router = APIRouter()

@router.post("/", response_model=Enrollment)
def enroll_user(enrollment: EnrollmentCreate):
    result = enrollment_service.enroll_user(enrollment.user_id, enrollment.course_id, user_service.users, course_service.courses)
    if not result:
        raise HTTPException(status_code=400, detail="Enrollment failed")
    return result

@router.put("/{enrollment_id}/complete", response_model=Enrollment)
def mark_complete(enrollment_id: int):
    enrollment = enrollment_service.mark_completed(enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.get("/user/{user_id}", response_model=list[Enrollment])
def get_user_enrollments(user_id: int):
    return enrollment_service.get_enrollments_by_user(user_id)

@router.get("/", response_model=list[Enrollment])
def get_all_enrollments():
    return enrollment_service.get_all_enrollments()