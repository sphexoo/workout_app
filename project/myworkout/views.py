import random


from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Exercise
from .forms import NumberOfExercisesForm


def index(request):
    exercises = Exercise.objects.all()
    form = NumberOfExercisesForm()
    context = {"exercises": exercises, "form": form}
    return render(request, "index.html", context=context)


def random_exercise(request):
    if request.method == "POST":
        form = NumberOfExercisesForm(request.POST)
        if not form.is_valid():
            form = NumberOfExercisesForm()
    else:
        return HttpResponseRedirect("/myworkout/")

    number_of_exercises = form.cleaned_data.get("number_of_exercises")

    if not number_of_exercises or number_of_exercises <= 0:
        return HttpResponseRedirect("/myworkout/")

    exercises = list(Exercise.objects.all())

    random_exercises = random.sample(exercises, number_of_exercises)
    context = {"random_exercises": random_exercises}

    return render(request, "random.html", context=context)
