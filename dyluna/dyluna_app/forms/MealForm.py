from django import forms
from ..models.MealModel import Meal

class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        exclude = ()

    def is_valid(self):
        return True