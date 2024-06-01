from django.contrib import admin

from .models import Exercise, TargetBodyPart, RequiredEquipment

admin.site.register(Exercise)
admin.site.register(TargetBodyPart)
admin.site.register(RequiredEquipment)

