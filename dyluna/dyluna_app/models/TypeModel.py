from django.db import models



class Type(models.Model): # czego to Type? :D TODO: zmienic nazwe na Workshop_Type
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name + " - ".join(self.description.split(" ")[0:7])
