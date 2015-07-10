from django.shortcuts import render
from django.views.generic.edit import CreateView
from .form import CreateArtistForm
# Create your views here.


class CreateArtistView(CreateView):
    template_name = 'register.html'
    form_class = CreateArtistForm