from django.db import models



class Preferences(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete="CASCADE")
    workshop = models.ForeignKey('Workshop', on_delete="CASCADE")

