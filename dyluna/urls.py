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
from .dyluna_app.views import Users_Display
from django.conf.urls.static import static

from dyluna.dyluna_app import views


urlpatterns = [
    url(r'^$', views.main ), #so just basically redirects

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^workshop/new/', views.new_workshop , name="new_workshop"),
    url(r'^diet/new/$', views.diet_new, name="diet_new "),
    # url(r'^diet/(?P<pk>\d+)$', views.DietDetailView.as_view(), name="diet_detail"),
    # url(r'^diet/$', views.DietListView.as_view(), name="diets"),

    url(r'^index', views.index ),

    url(r'^admin', admin.site.urls, name='admin_panel'),
    url(r'^main', views.main, name="main" ),
    url('list', views.list, name='list'),
    url('menu', Users_Display.as_view()),
    url(r'^students', views.users_students  ),
    url(r'^teachers', views.users_teachers  ),
    url(r'^workshop', views.workshop  ),
    url('schedules', views.workshop_schedule  ),
    url(r'^meals', views.meal  ),

    url(r'^accounts/', include('django.contrib.auth.urls') )

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# TODO: Add function to generate urls to: new and displays - those are generics