from django.db import models


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name + " ".join(self.description.split(" ")[0:7])

