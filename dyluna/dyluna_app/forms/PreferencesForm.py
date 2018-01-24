from django import forms
from ..models.PreferencesModel import Preferences

class PreferencesForm(forms.ModelForm):

    class Meta:
        model = Preferences
        exclude = ()

