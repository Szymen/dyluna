from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse
from .models.models import User
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello world!")


def blank(request):
    return HttpResponse("Welcome on blank page")


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