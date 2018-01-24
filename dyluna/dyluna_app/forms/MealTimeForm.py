from django import forms
from ..models.Meal_TimeModel import Meal_Time

class MealTimeForm(forms.ModelForm):

    class Meta:
        model = Meal_Time
        exclude = ()
