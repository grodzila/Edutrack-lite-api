from datetime import date

enrollments = []
enrollment_id_counter = 1

def enroll_user(user_id, course_id, users, courses):
    global enrollment_id_counter
    user = next((u for u in users if u["id"] == user_id and u["is_active"]), None)
    course = next((c for c in courses if c["id"] == course_id and c["is_open"]), None)
    if not user or not course:
        return None
    if any(e for e in enrollments if e["user_id"] == user_id and e["course_id"] == course_id):
        return None
    enrollment = {
        "id": enrollment_id_counter,
        "user_id": user_id,
        "course_id": course_id,
        "enrolled_date": date.today(),
        "completed": False
    }
    enrollments.append(enrollment)
    enrollment_id_counter += 1
    return enrollment

def mark_completed(enrollment_id):
    enrollment = next((e for e in enrollments if e["id"] == enrollment_id), None)
    if enrollment:
        enrollment["completed"] = True
    return enrollment

def get_enrollments_by_user(user_id):
    return [e for e in enrollments if e["user_id"] == user_id]

def get_all_enrollments():
    return enrollments