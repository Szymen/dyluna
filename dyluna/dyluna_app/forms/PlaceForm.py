from django import forms
from ..models.PlaceModel import Place

class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        exclude = ()

    def is_valid(self):
        return True