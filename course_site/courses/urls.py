from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.programs, name="programs"),  # show all programs
    path('programs/<int:program_id>', views.single_program, name="single-program"),
    path('course/', views.courses, name="courses"),  # show all courses
    path('course/<int:course_id>', views.single_course, name="single-course"),
    path('course/<int:course_id>/<str:chapter_name>', views.chapter, name="chapter"),  # show one chapter
    path('course/<int:course_id>/<str:chapter_name>/<str:lecture_name>', views.lecture, name="lecture"),
    # show lecture, along with videos and notes
]
