from django.db import models



class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.CharField(max_length=255)

