from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from .forms.forms import DietForm

from .models.models import *

from .models.models import User
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello world!")


def blank(request):
    return HttpResponse("Welcome on blank page")


def diet_new(request):
    form = DietForm()
    return render(request, '../templates/form_template.html', {'form': form, 'name': 'diet'})


def diet_new(request):
    if request.method == "POST":
        form = DietForm(request.POST)
        if form.is_valid():
            print(form)
            diet = form.save()
            return redirect('diet_detail', pk=diet.pk)
    else:
        form = DietForm()
    return render(request, 'templates/form_template.html', {'form': form})


class DietListView(ListView):
    model = Diet
    template_name = 'templates/list_template.html'


class DietDetailView(DetailView):
    model = Diet
    template_name = 'templates/detail_template.html'


def main(request):
    return render(request, 'main.html')


def users(request):
    return render(request, 'users.html', {
        'users': User.objects.all()
    })


def users_students(request):
    return render(request, 'menu_users_students.html', {
        'users': User.objects.filter(user_role__role_name="UCZESTNIK")
    })


def users_teachers(request):
    return render(request, 'menu_users_teachers.html', {
        'users': User.objects.filter(user_role__role_name="KOORDYNATOR")
    })


def workshop(request):
    return HttpResponse("Workshops")


def workshop_schedule(request):
    return HttpResponse("Workshop Schedules")

