from django.db import models

from dyluna.dyluna_app.models.UserModel import User
from dyluna.dyluna_app.models.WorkshopModel import Workshop


class Preferences(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete="CASCADE")
    workshop = models.ForeignKey(Workshop, on_delete="CASCADE")

