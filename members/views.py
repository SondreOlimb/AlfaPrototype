
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

def default_map(request):
        # TODO: move this token to Django settings from an environment variable
        # found in the Mapbox account settings and getting started instructions
        # see https://www.mapbox.com/account/ under the "Access tokens" section
        mapbox_access_token = 'pk.my_mapbox_access_token'
        return render(request, 'article_detail.html.html',
                      {'mapbox_access_token': mapbox_access_token})
