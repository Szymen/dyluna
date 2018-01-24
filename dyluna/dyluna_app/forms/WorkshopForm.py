from django import forms
from ..models.WorkshopModel import Workshop


class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        exclude = ()