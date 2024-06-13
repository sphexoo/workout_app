from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.random_exercise, name="random_exercise"),
    path("timer/", views.workout_timer, name="workout_timer"),
]
