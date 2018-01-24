from django.db import models

from dyluna.dyluna_app.models.DietModel import Diet
from dyluna.dyluna_app.models.User_RoleModel import User_Role


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    diet = models.ForeignKey(Diet, on_delete="CASCADE", null=True)
    user_role = models.ForeignKey(User_Role, on_delete="CASCADE")

    def __str__(self):
        return self.name + " " + self.last_name

    def is_valid(self):
        return True