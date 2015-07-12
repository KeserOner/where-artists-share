from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .form import CreateArtistForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


class CreateArtistView(CreateView):
    template_name = 'register.html'
    form_class = CreateArtistForm

def artist_login(request):
    print('lol')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            login(request, form.user_cache)
            return HttpResponseRedirect('artist/register')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form' : form})
