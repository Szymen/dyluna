from django import forms
from ..models.UserModel import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        # exclude = ( 'user_role', )
        exclude = ()

    def is_valid(self):
        return True
