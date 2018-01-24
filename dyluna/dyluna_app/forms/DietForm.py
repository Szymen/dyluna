from django import forms
from ..models.DietModel import Diet

class DietForm(forms.ModelForm):

    class Meta:
        model = Diet
        exclude = ()
        # exclude = (id, )


