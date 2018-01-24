from django.db import models


class Workshop_Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    workshop = models.ForeignKey('Workshop', on_delete="CASCADE")
    workshop_time = models.DateTimeField()
    places = models.ManyToManyField('Place')
