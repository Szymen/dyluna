

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
# from ..models impor


db_logger = logging.getLogger('db')


from django.contrib.auth.decorators import login_required



class Users_Display(View):

    def get(self, request):
        return render(request, 'users.html', {
        'users': UserModel.User.objects.all()
        })


class Users_Filter_Display(ListView):

    context_object_name = 'users'
    template_name = 'menu_users_students.html'


    def get_queryset(self):
        self.user_role__role_name = get_object_or_404(UserModel, name=self.kwargs['user_role'])
        return UserModel.User.objects.filter(user_role__role_name=self.user_role__role_name)

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
        'users': UserModel.User.objects.filter(user_role__role_name="UCZESTNIK")
    })

@login_required
def users_teachers(request):
    return render(request, 'menu_users_teachers.html', {
        'users': UserModel.User.objects.filter(user_role__role_name="KOORDYNATOR")
    })


@login_required
def new_user(request):
    if request.method == "POST":
        form = UserForm.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse("Nowy uczestnik utworzony <a href='/main'>Wróc do menu głownego</a>")
            # return redirect('diet_detail', pk=diet.pk)
    else:
        form = UserForm.UserForm()
    return render(request, 'form_template.html', {'form': form, 'name': "Uczestnika"})
