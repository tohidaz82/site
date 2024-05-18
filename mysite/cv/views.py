from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile
from django.urls import reverse_lazy

# Create your views here.

class Students(ListView):
    model = Profile
    template_name = 'template.html'


class information(DetailView):
    model = Profile
    template_name = 'information.html'

class ProfileView(CreateView):
    model = Profile
    template_name = 'new.html'
    fields = ['name', 'phone', 'email', 'skills', 'education', 'experience' ]


class ProfileUpdate(UpdateView):
    model = Profile
    template_name = 'edit.html'
    fields = ['name', 'phone', 'email', 'skills', 'education', 'experience' ]


class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'delete.html'
    success_url = reverse_lazy('students')