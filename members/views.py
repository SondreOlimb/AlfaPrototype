
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404
from .forms import SignUpForms,EditProfileForm,PasswordChangeingForms
from django.views.generic import DetailView
from blog.models import Profile

class ShowProfilePageView(DetailView):
    model = Profile
    template_name =  "user_profile.html"

    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data

        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context




class UserRegisterView(generic.CreateView):
    form_class = SignUpForms
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("landing")

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangeingForms
    success_url = reverse_lazy("password_success")

def password_success(request):
    return render(request,"registration/password_succsess.html",{})



