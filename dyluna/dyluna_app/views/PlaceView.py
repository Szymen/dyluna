

from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponse
from django.views import View
from ..models import UserModel, WorkshopModel, Workshop_ScheduleModel, PlaceModel, Meal_TimeModel, PreferencesModel, MealModel
from ..forms import DietForm, UserForm, WorkshopForm, WorkshopSchedulesForm, PreferencesForm, MealTimeForm, MealForm, PlaceForm, TypeForm, EquipmentForm
from django.views.generic import ListView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import logging
import MySQLdb

db_logger = logging.getLogger('db')


from django.contrib.auth.decorators import login_required


@login_required
def place(request):
    return render(request, 'places.html', {
        'places': PlaceModel.Place.objects.all()
    })


@login_required
def new_place(request):
    if request.method == "POST":
        form = PlaceForm.PlaceForm(request.POST)
        if form.is_valid():
            place = form.save()
            return HttpResponse("Nowe miejsce utworzone <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = PlaceForm.PlaceForm()
    return render(request, 'form_template.html', {'form': form, 'name': "Miejsce"})

