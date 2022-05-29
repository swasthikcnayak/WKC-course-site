from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@login_required
def programs(request):
    programs = Program.objects.all()
    courses = Course.objects.all()
    return {programs, courses}


@login_required
def courses(request):
    return Course.objects.all()


@login_required
def chapter(request):
    return Chapters.objects.all()


@login_required
def lecture(request):
    return Lecture.objects.all(0)


@login_required
def singleProgram(request):
    pass


@login_required
def singleCourse(request):
    pass
