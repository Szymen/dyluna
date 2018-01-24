"""dyluna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from .dyluna_app.views import views_handler
from django.conf.urls.static import static


from dyluna.dyluna_app.views import MenuView
from dyluna.dyluna_app.views import WorkshopView
from dyluna.dyluna_app.views import UserView
from dyluna.dyluna_app.views import Workshop_scheduleView
from dyluna.dyluna_app.views import PreferencesView
from dyluna.dyluna_app.views import MealView
from dyluna.dyluna_app.views import Meal_timeView
from dyluna.dyluna_app.views import TypeView
from dyluna.dyluna_app.views import PlaceView
from dyluna.dyluna_app.views import EquipmentView
from dyluna.dyluna_app.views import DietView


urlpatterns = [

    url(r'^signup/$', MenuView.signup, name='signup'),
    url(r'^info_about/$', MenuView.info_about, name='info_about'),

    url(r'^workshop/new/', WorkshopView.new_workshop , name="new_workshop"),
    url(r'^new', MenuView.new_things , name="new_things"),
    url(r'^user/new', UserView.new_user , name="new_user"),
    url(r'^diet/new', DietView.new_diet, name="new_diet"),
    url(r'^workshop_schedule/new', Workshop_scheduleView.new_workshop_schedule, name="new_workshop_schedule"),
    url(r'^preferences/new', PreferencesView.new_preferences, name="new_preferences"),
    url(r'^meal/new', MealView.new_meal, name="new_meal"),
    url(r'^meal_time/new', Meal_timeView.new_meal_time, name="new_meal_time"),
    url(r'^type/new', TypeView.new_type, name="new_type"),
    url(r'^place/new', PlaceView.new_place, name="new_place"),
    url(r'^equipment/new', EquipmentView.new_equipment, name="new_equipment"),

    # url(r'^diet/(?P<pk>\d+)$', views.DietDetailView.as_view(), name="diet_detail"),
    # url(r'^diet/$', views.DietListView.as_view(), name="diets"),

    url(r'^index', MenuView.index ),

    url(r'^admin', admin.site.urls, name='admin_panel'),
    url(r'^main', MenuView.main, name="main" ),
    url('list', MenuView.list, name='list'),


    url('menu', UserView.Users_Display.as_view()),
    url(r'^students', UserView.users_students),
    url(r'^teachers', UserView.users_teachers),
    url(r'^workshop', WorkshopView.workshop),
    url('schedules', Workshop_scheduleView.workshop_schedule),
    url(r'^meals', MealView.meal),
    url(r'^places', PlaceView.place),
    url(r'^preferences', PreferencesView.preference),

    url(r'^accounts/', include('django.contrib.auth.urls') ),

    url(r'^$', MenuView.index),  # so just basically redirects

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# TODO: Add function to generate urls to: new and displays - those are generics