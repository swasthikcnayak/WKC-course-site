from django.contrib import admin

# Register your models here.
from .models import Program, Course, Lecture, Videos, Notes


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    pass


@admin.register(Videos)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    pass
