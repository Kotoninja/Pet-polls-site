from django.contrib import admin
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="home"),
    path("/question/<int:question_id>", views.question_window, name="question"),
    path("/create-question", views.create_question,name = 'create_question')
]
