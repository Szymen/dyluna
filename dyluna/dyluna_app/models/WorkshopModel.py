from django.db import models

from dyluna.dyluna_app.models.EquipmentModel import Equipment
from dyluna.dyluna_app.models.TypeModel import Type
from dyluna.dyluna_app.models.UserModel import User

class Workshop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete="CASCADE") # TODO: to jest prowadzący, zmienic nazwe odpowiednio
    type = models.ForeignKey(Type, on_delete="CASCADE")
    description = models.CharField(max_length=1000, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete="CASCADE", null=True)

    def __str__(self):
        return "[{0}] {1} - {2}".format( str(self.id), self.name, str(self.type) )

    def is_valid(self):
        return True