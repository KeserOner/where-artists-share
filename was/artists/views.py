from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from .form import CreateArtistForm, UpdateArtistForm, Artists
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect


class CreateArtistView(CreateView):
    template_name = 'register.html'
    form_class = CreateArtistForm
    success_url = '/'


class UpdateArtistView(UpdateView):
    template_name = 'register.html'
    form_class = UpdateArtistForm
    success_url = '/'

    def get_queryset(self):
        artist = Artists.objects.filter(user=self.request.user).values_list('id', flat=True)
        return artist[0]
        #lol = get_object_or_404(Artists, pk=artist[0])
        #print(type(lol))



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