courses = []
course_id_counter = 1

def create_course(course_data):
    global course_id_counter
    course = {**course_data.dict(), "id": course_id_counter, "is_open": True}
    courses.append(course)
    course_id_counter += 1
    return course

def get_course(course_id):
    return next((c for c in courses if c["id"] == course_id), None)

def get_all_courses():
    return courses

def update_course(course_id, course_data):
    course = get_course(course_id)
    if course:
        course.update(course_data.dict())
    return course

def delete_course(course_id):
    global courses
    courses = [c for c in courses if c["id"] != course_id]

def close_enrollment(course_id):
    course = get_course(course_id)
    if course:
        course["is_open"] = False
    return course

def get_users_enrolled(course_id, enrollments, users):
    return [u for u in users if any(e["course_id"] == course_id and e["user_id"] == u["id"] for e in enrollments)]