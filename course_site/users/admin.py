from django.contrib import admin

# Register your models here.
from course_site.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass