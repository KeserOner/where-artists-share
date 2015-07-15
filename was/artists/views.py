from django.shortcuts import render
from django.views.generic.edit import CreateView
from .form import CreateArtistForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect


class CreateArtistView(CreateView):
    template_name = 'register.html'
    form_class = CreateArtistForm
    success_url = '/'

def artist_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            login(request, form.user_cache)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form' : form})

def artist_logout(request):
    logout(request)
    return HttpResponseRedirect('/')