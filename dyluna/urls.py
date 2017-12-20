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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from dyluna.dyluna_app import views


urlpatterns = [
    url(r'^$', views.blank  ),

    url(r'^diet/new/$', views.diet_new, name="diet_new "),
    url(r'^diet/(?P<pk>\d+)$', views.DietDetailView.as_view(), name="diet_detail"),
    url(r'^diet/$', views.DietListView.as_view(), name="diets"),

    url(r'^index', views.index ),

    url(r'^admin', admin.site.urls, name='admin_panel'),
    url(r'^main', views.main  ),
    url(r'^menu/users', views.users  ),
    url(r'^menu/users/students', views.users_students  ),
    url(r'^menu/users/teachers', views.users_teachers  ),
    url(r'^menu/workshop', views.workshop  ),
    url(r'^menu/workshop_schedules', views.workshop_schedule  ),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)