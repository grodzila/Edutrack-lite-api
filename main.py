from fastapi import FastAPI
from routes import user_routes, course_routes, enrollment_routes

app = FastAPI(title="EduTrack Lite API")

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(course_routes.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollment_routes.router, prefix="/enrollments", tags=["Enrollments"])

        