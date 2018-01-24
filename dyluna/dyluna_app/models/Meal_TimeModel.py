from django.db import models



class Meal_Time(models.Model):
    meal = models.OneToOneField(
        'Meal',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    meal_time = models.DateTimeField()

