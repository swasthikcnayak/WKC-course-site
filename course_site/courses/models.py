from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)


class Course(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    program = models.ManyToManyField(Program)
    description = models.TextField()


class Chapters(models.Model):
    chapterName = models.CharField(max_length=50, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    knowledgeLevel = models.IntegerField(default=5, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    description = models.TextField()


class Lecture(models.Model):
    lectureName = models.CharField(max_length=50, null=False, blank=False)
    chapter = models.ForeignKey(Chapters,on_delete=models.CASCADE)
    description = models.TextField()


class Notes(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    notes = models.FileField(upload_to="Notes/")


class Videos(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    link = models.URLField()

