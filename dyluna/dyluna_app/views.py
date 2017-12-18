from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello world!")


