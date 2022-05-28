from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create-course/', views.user_login, name='create-course'),

]
