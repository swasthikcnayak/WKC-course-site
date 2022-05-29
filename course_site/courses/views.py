from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@login_required
def programs(request):
    # shows all the programs available in the db, also the courses that are linked wit the program
    return Program.objects.all()


@login_required
def single_program(request, program_id):
    # gives total description of one particular program, all the courses, how many chapters are there, how many lectures
    # are there etc
    program = Program.objects.filter(id=id)
    return program


@login_required
def courses(request):
    # shows all the courses available in the db
    # also the programs that particular course is part of, user can choose to take the course
    return Course.objects.all()


@login_required
def single_course(request, course_id):
    # gives total description of one particular course, how many chapters are there, how many lectures are there etc
    course = Course.objects.filter(id=course_id)
    return course


@login_required
def chapter(request, course_id, chapter_name):
    # shows one particular chapter, a chapter can have multiple lectures.
    chapter_ref = Chapters.objects.filter(chapterName=chapter_name, course__id=course_id)
    return chapter_ref


@login_required
def lecture(request, course_id, chapter_name, lecture_name):
    # shows one particular lecture, along with video and notes part of the lecture
    chapter_ref = chapter(request, course_id, chapter_name)
    lecture_ref = Lecture.objects.filter(lectureName=lecture_name, chapter__id=chapter_ref.id)
    notes = Notes.objects.filter(lecture__id=lecture_ref.id)
    videos = Videos.objects.filter(lecture__id=lecture_ref.id)
    return {lecture_ref, notes, videos}
