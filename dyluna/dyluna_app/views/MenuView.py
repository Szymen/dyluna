from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponse
from django.views import View
# from .models.models import User, Workshop, Workshop_Schedule, Place, Meal_Time, Preferences
# from .forms.forms import DietForm, UserForm, WorkshopForm, WorkshopSchedulesForm, PreferencesForm, MealTimeForm, MealForm, PlaceForm, TypeForm, EquipmentForm
from django.views.generic import ListView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import logging
import MySQLdb

db_logger = logging.getLogger('db')


from django.contrib.auth.decorators import login_required



def index(request):
    # html = "<a href='/info_about'>Go to info page</a> "
    # return HttpResponse(html)
    return redirect(info_about)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def main(request):
    return render(request, 'main.html')

@login_required
def list(request):
    return render(request, 'list_template.html')

@login_required
def new_things(request):
    return render(request, 'new_things.html')


def info_about(request):
    return render(request, 'info_about.html')


