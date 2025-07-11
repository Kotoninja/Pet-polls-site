from django.contrib import admin
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.home, name="home"),
    path("question/<int:question_id>", views.question_page, name="question"),
    path("create-question", views.create_question,name = 'create_question'),
    path("base",views.base, name = 'base')
]
