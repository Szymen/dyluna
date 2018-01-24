from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponse
from django.views import View
from .models.models import User, Workshop, Workshop_Schedule
from .forms.forms import DietForm, UserForm, WorkshopForm
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
    print (Workshop_Schedule.objects.all())
    db = MySQLdb.connect(host="localhost", user="dyluna",
                        passwd="haslo123", db="dyluna")
    cr = db.cursor()
    data = cr.execute('''SELECT sch.id, sch.workshop_time, sch.workshop_id, pl.name FROM dyluna_app_workshop_schedule AS sch 
        INNER JOIN dyluna_app_workshop_schedule_places AS schpl ON sch.id = schpl.workshop_schedule_id 
        INNER JOIN dyluna_app_place AS pl ON schpl.id = pl.id''')
    #data = cr.fetchall()
    print ("NANANANANANANANANANANANANANA\n\n\n\n\n")
    print (data)
    #print (data)
    return render(request, 'workshop_schedule.html', {
        'schedules': data
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
