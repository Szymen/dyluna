from django import forms
from ..models.WorkshopModel import Workshop


class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        exclude = ()

    def is_valid(self):
        return True