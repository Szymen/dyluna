from django import forms
from django.contrib.auth.models import User as authUser
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


class loginUserForm(forms.ModelForm):

    class Meta:
        model = authUser
        exclude = ()