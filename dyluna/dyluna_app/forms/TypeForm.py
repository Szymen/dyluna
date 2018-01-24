from django import forms
from ..models.TypeModel import Type

class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        exclude = ()