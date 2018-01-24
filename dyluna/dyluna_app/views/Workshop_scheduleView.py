

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
def new_workshop_schedule(request):
    if request.method == "POST":
        form = WorkshopSchedulesForm.WorkshopSchedulesForm(request.POST)
        if form.is_valid():
            workshop_schedule = form.save()
            return HttpResponse("Nowy harmonoram utworzony <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = WorkshopSchedulesForm.WorkshopSchedulesForm()
    return render(request, 'form_template.html', {'form': form, 'name': "Harmonogram"})



@login_required
def workshop_schedule(request):
    return render(request, 'workshop_schedule.html', {
        'schedules': Workshop_ScheduleModel.Workshop_Schedule.objects.raw('''SELECT sch.id, sch.workshop_time, sch.workshop_id, schpl.id, pl.name FROM dyluna_app_workshop_schedule_places AS schpl
INNER JOIN dyluna_app_workshop_schedule AS sch ON sch.id = schpl.workshop_schedule_id 
INNER JOIN dyluna_app_place AS pl ON schpl.id = pl.id'''),
        'places': PlaceModel.Place.objects.raw('''SELECT sch.id, sch.workshop_time, sch.workshop_id, schpl.id, pl.name FROM dyluna_app_workshop_schedule_places AS schpl
INNER JOIN dyluna_app_workshop_schedule AS sch ON sch.id = schpl.workshop_schedule_id 
INNER JOIN dyluna_app_place AS pl ON schpl.id = pl.id''')
    })

