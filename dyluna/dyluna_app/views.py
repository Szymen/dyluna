from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponse
from django.views import View
from .models.models import User, Workshop, Workshop_Schedule, Place, Meal_Time, Preferences
from .forms.forms import DietForm, UserForm, WorkshopForm, WorkshopSchedulesForm, PreferencesForm, MealTimeForm, MealForm, PlaceForm, TypeForm
from django.views.generic import ListView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import logging
import MySQLdb

db_logger = logging.getLogger('db')


from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello world!")


@login_required
def diet_new(request):
    if request.method == "POST":
        form = DietForm(request.POST)
        if form.is_valid():
            diet = form.save()
            return HttpResponse("Nowa dieta utworzona <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = DietForm()
    return render(request, 'templates/form_template.html', {'form': form, 'name': "diet"})


@login_required
def main(request):
    return render(request, 'main.html')

@login_required
def list(request):
    return render(request, 'list_template.html')

@login_required
def new_things(request):
    return render(request, 'new_things.html')


class Users_Display(View):

    def get(self, request):
        return render(request, 'users.html', {
        'users': User.objects.all()
        })


class Users_Filter_Display(ListView):

    context_object_name = 'users'
    template_name = 'menu_users_students.html'


    def get_queryset(self):
        self.user_role__role_name = get_object_or_404(User, name=self.kwargs['user_role'])
        return User.objects.filter(user_role__role_name=self.user_role__role_name)

    '''def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['role_user'] = self.user_role__role_name
        return context

    def get(self, request):
        return render(request, 'menu_users_students.html', {
            'users': self.get_context_data()
        })'''


@login_required
def users_students(request):
    return render(request, 'menu_users_students.html', {
        'users': User.objects.filter(user_role__role_name="UCZESTNIK")
    })

@login_required
def users_teachers(request):
    return render(request, 'menu_users_teachers.html', {
        'users': User.objects.filter(user_role__role_name="KOORDYNATOR")
    })


@login_required
def workshop(request):
    try:
        1/0
    except Exception as e:
        db_logger.exception(e)
    return render(request, 'workshop.html', {
        'workshops': Workshop.objects.all()
    })

@login_required
def workshop_schedule(request):
    return render(request, 'workshop_schedule.html', {
        'schedules': Workshop_Schedule.objects.raw('''SELECT sch.id, sch.workshop_time, sch.workshop_id, schpl.id, pl.name FROM dyluna_app_workshop_schedule_places AS schpl
INNER JOIN dyluna_app_workshop_schedule AS sch ON sch.id = schpl.workshop_schedule_id 
INNER JOIN dyluna_app_place AS pl ON schpl.id = pl.id'''),
        'places': Place.objects.raw('''SELECT sch.id, sch.workshop_time, sch.workshop_id, schpl.id, pl.name FROM dyluna_app_workshop_schedule_places AS schpl
INNER JOIN dyluna_app_workshop_schedule AS sch ON sch.id = schpl.workshop_schedule_id 
INNER JOIN dyluna_app_place AS pl ON schpl.id = pl.id''')
    })

@login_required
def meal(request):
    return render(request, 'meal.html', {
        'meals': Meal_Time.objects.all()
    })

@login_required
def place(request):
    return render(request, 'places.html', {
        'places': Place.objects.all()
    })

@login_required
def preference(request):
    return render(request, 'preferences.html', {
        'preferences': Preferences.objects.all()
    })

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
def new_workshop(request):
    if request.method == "POST":
        form = WorkshopForm(request.POST)
        if form.is_valid():
            workshop = form.save()
            return HttpResponse("Nowe zajęcia utworzone <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = WorkshopForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Zajęcia"})


@login_required
def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse("Nowy uczestnik utworzony <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = UserForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Uczestnika"})


@login_required
def new_diet(request):
    if request.method == "POST":
        form = DietForm(request.POST)
        if form.is_valid():
            diet = form.save()
            return HttpResponse("Nowa dieta utworzona <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = DietForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Dietę"})


@login_required
def new_workshop_schedule(request):
    if request.method == "POST":
        form = WorkshopSchedulesForm(request.POST)
        if form.is_valid():
            workshop_schedule = form.save()
            return HttpResponse("Nowy harmonoram utworzony <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = WorkshopSchedulesForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Harmonogram"})


@login_required
def new_preferences(request):
    if request.method == "POST":
        form = PreferencesForm(request.POST)
        if form.is_valid():
            preference = form.save()
            return HttpResponse("Nowe preferencje utworzone <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = PreferencesForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Preferencje"})


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
    return render(request, 'form_template.html', {'form': form, 'name':"Posiłek"})


@login_required
def new_meal_time(request):
    if request.method == "POST":
        form = MealTimeForm(request.POST)
        if form.is_valid():
            meal_time = form.save()
            return HttpResponse("Nowy posiłek utworzony <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = MealTimeForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Czas posiłku"})


@login_required
def new_type(request):
    if request.method == "POST":
        form = TypeForm(request.POST)
        if form.is_valid():
            type = form.save()
            return HttpResponse("Nowy typ zajęć utworzony <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = TypeForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Typ Zajęć"})


@login_required
def new_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save()
            return HttpResponse("Nowe miejsce utworzone <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = PlaceForm()
    return render(request, 'form_template.html', {'form': form, 'name':"Miejsce"})
