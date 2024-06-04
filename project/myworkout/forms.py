from django import forms


class NumberOfExercisesForm(forms.Form):
    number_of_exercises = forms.IntegerField(
        label="Number of Exercises",
        min_value=1,
        max_value=10,
        initial=3,
    )
