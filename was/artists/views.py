from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect

from .form import CreateArtistForm, UpdateArtistForm, Artists, User
from photo.models import Photo


class CreateArtistView(CreateView):
    template_name = 'register.html'
    form_class = CreateArtistForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(CreateArtistView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class UpdateArtistView(UpdateView):
    template_name = 'update.html'
    form_class = UpdateArtistForm
    success_url = '/artist/profile'

    def get_initial(self):
        initial = {}
        user = User.objects.get(username=self.request.user.username)
        initial['username'] = user.username
        initial['email'] = user.email
        return initial

    def get_object(self):
        return get_object_or_404(Artists, user=self.request.user)


def artist_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            login(request, form.user_cache)
            return HttpResponseRedirect('/artist/profile')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def artist_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def artist_delete(request):
    user = User.objects.get(username=request.user.username)
    user.delete()
    return HttpResponseRedirect('/')


@login_required
def profile_page(request):
    artist = Artists.objects.get(user=request.user)
    photos = Photo.objects.filter(artist=artist)
    return render(request, 'profile.html', {
                  'artist': artist,
                  'photos': photos,
                  })