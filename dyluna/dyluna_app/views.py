from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from .forms.forms import DietForm

from .models.models import *


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
            diet = form.save(commit=False)
            diet.name = form.name
            diet.description = form.description
            diet.save()
            return redirect('diet_detail', id=diet.pk)
    else:
        form = DietForm()
    return render(request, 'templates/form_template.html', {'form': form})


# def diet_detail(request, pk):
#     diet = get_object_or_404(Diet,  id=pk)
#     return render( request, 'templates/detail_template.html', {'data': diet})


class DietListView(ListView):
    model = Diet
    template_name = '../templates/list_template.html'


class DietDetailView(DetailView):
    model = Diet
    template_name = '../templates/detail_template.html'
