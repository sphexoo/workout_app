import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
import django_tables2 as tables

from .models import Exercise
from .forms import NumberOfExercisesForm
from .tables import ExercisesTable



def index(request):
    exercises = Exercise.objects.all()
    form = NumberOfExercisesForm()
    table = ExercisesTable(exercises)
    # table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {"form": form, "table": table}
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
