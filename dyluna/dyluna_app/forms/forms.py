from django import forms
from django.contrib.auth.models import User as authUser
from ..models.models import *

class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        exclude = ()


class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        exclude = ()


class MealTimeForm(forms.ModelForm):

    class Meta:
        model = Meal_Time
        exclude = ()


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        exclude = ()


class PreferencesForm(forms.ModelForm):

    class Meta:
        model = Preferences
        exclude = ()


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        exclude = ()


class WorkshopSchedulesForm(forms.ModelForm):

    class Meta:
        model = Workshop_Schedule
        exclude = ()


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


class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        exclude = ()