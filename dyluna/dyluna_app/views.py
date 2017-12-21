from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponse
from django.views import View
from .models.models import User, Workshop
from .forms.forms import DietForm, UserForm, WorkshopForm
from django.views.generic import ListView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


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
    return render(request, 'templates/form_template.html', {'form': form, 'name':"diet"})


@login_required
def main(request):
    return render(request, 'main.html')


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
    return render(request, 'workshop.html', {
        'workshops': Workshop.objects.all()
    })

@login_required
def workshop_schedule(request):
    return HttpResponse("Workshop Schedules")


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
    return render(request, 'templates/form_template.html', {'form': form, 'name':"Zajęcia"})
