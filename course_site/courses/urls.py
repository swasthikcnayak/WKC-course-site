from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.programs, name="programs"),  # show all programs
    path('programs/<int:id>', views.singleProgram, name="single-program"),
    path('course/', views.courses, name="courses"),  # show all courses
    path('course/<int:id>', views.singleCourse, name="single-course"),
    path('course/<int:courseId>/<str:chapterName>', views.chapter, name="chapter"),  # show one chapter
    path('course/<int:courseId>/<str:chapterName>/<str:lectureName>', views.lecture, name="lecture"),
    # show lecture, along with videos and notes
]
