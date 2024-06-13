import django_tables2 as tables

from .models import Exercise


class ExercisesTable(tables.Table):

    class Meta:
        order_by = "name"
        model = Exercise
        fields = ("name", "required_equipment", "target_body_part")
        attrs = {"class": "style"}
        orderable = False
        
