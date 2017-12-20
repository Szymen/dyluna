from django import forms

from ..models.models import *


class DietForm(forms.ModelForm):

    class Meta:
        model = Diet
        exclude = (id, )