from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from .models import models


# login: admin
# pass : haslo123

# Register your models here.

# admin.site.register(models.przykladowa_osoba)
# admin.site.register(models.)

app_models = apps.get_app_config('dyluna_app').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
# class User(models.Model):
#
# class User_Role(models.Model):
#
#
# class Diet(models.Model):
#
# class Workshop(models.Model):
#
# class Type(models.Model):
#
# class Workshop_Schedule(models.Model):
#
#
# class Equipment(models.Model):
#
# class Place(models.Model):
#
#
# class Meal(models.Model):
#
#
# class Meal_Time(models.Model):
#
#
# class Preferences(models.Model):