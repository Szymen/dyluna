from django.db import models

from dyluna.dyluna_app.models.WorkshopModel import Workshop
from dyluna.dyluna_app.models.PlaceModel import Place


class Workshop_Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    workshop = models.ForeignKey(Workshop, on_delete="CASCADE")
    workshop_time = models.DateTimeField()
    places = models.ManyToManyField(Place)

    def is_valid(self):
        return True