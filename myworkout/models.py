from django.db import models


class TargetBodyPart(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RequiredEquipment(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField("Created on")
    target_body_part = models.ManyToManyField(TargetBodyPart)
    required_equipment = models.ManyToManyField(RequiredEquipment, blank=True)

    def __str__(self):
        return self.name
