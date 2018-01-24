from django.db import models


class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name + " - " + "".join(self.description.split(" ")[0:7])
