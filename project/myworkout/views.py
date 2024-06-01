from django.shortcuts import render
from django.http import HttpResponse

from .models import Exercise


def index(request):
    exercises = Exercise.objects.all()
    context = {"exercises": exercises}
    return render(request, "list.html", context=context)
