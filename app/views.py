from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *

class Trainers_list(ListView):
    model=Trainer
    template_name='Trainers_list.html'
    context_object_name='t1'
    ordering=['trainer_name']