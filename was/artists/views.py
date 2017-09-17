from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from photo.models import Photo
from photo.forms import UploadPhotoForm

from .form import CreateArtistForm, UpdateArtistForm, Artists, User


class CreateArtistView(CreateView):
    template_name = 'register.html'
    form_class = CreateArtistForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(CreateArtistView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)

        return valid


class UpdateArtistView(UpdateView):
    template_name = 'update.html'
    form_class = UpdateArtistForm

    def get_initial(self):
        initial = {}
        user = User.objects.get(username=self.request.user.username)

        initial['username'] = user.username
        initial['email'] = user.email

        return initial

    def get_object(self):
        return get_object_or_404(Artists, user=self.request.user)

    def get_success_url(self):
        return reverse('profile_page', kwargs={'user_pk': self.object.user.pk})


def artist_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            login(request, form.user_cache)

            return HttpResponseRedirect(
                reverse(
                    'profile_page',
                    kwargs={'user_pk': form.user_cache.pk}
                )
             )
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
def follow_artist(request, **kwargs):
    artist = Artists.objects.get(user=request.user)
    artist_pk = kwargs.get('artist_pk', '')
    artist_followed = get_object_or_404(Artists, pk=artist_pk)

    artist.artists_followed.add(artist_followed)

    return HttpResponseRedirect(
        request.META.get(
            'HTTP_REFERER',
            '/artist/profile'
        )
    )


class ProfilePage(DetailView):
    model = Artists
    context_object_name = 'artist'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        photos = Photo.objects.filter(artist=self.object)
        context['photos'] = photos

        if self.request.user == self.object.user:
            context['is_user'] = True
            context['form'] = UploadPhotoForm()
        else:
            context['is_user'] = False

        return context

    def get_object(self):
        return self.get_queryset()

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk', '')
        artist = get_object_or_404(Artists, user__pk=user_pk)

        return artist
