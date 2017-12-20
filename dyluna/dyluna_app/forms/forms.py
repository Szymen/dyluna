from django import forms

from ..models.models import *


class DietForm(forms.ModelForm):

    class Meta:
        model = Diet
        exclude = ()
        # exclude = (id, )


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        # exclude = ( 'user_role', )
        exclude = ()