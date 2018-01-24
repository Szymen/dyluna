from django import forms
from ..models.EquipmentModel import Equipment


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        exclude = ()

    def is_valid(self):
        return True