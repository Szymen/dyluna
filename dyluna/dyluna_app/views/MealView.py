

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
def meal(request):
    return render(request, 'meal.html', {
        'meals': Meal_TimeModel.Meal_Time.objects.all()
    })

@login_required
def new_meal(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save()
            return HttpResponse("Nowy posiłek utworzony <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = MealForm()
    return render(request, 'form_template.html', {'form': form, 'name': "Posiłek"})
