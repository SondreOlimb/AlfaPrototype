
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404
from .forms import SignUpForms,EditProfileForm,PasswordChangeingForms,EditProfilePageForm, ProfilePageForm
from django.views.generic import DetailView,CreateView
from blog.models import Profile, Post,Shoe


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = "registration/create_user_profile_page.html"
    form_class = ProfilePageForm

    def form_valid(self, form): #make user id avalibol to user
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    success_url = reverse_lazy("landing")
    form_class = EditProfilePageForm



class ShowProfilePageView(DetailView):
    model = Profile
    template_name =  "user_profile.html"

    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data

        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs["pk"])
        shoes = Shoe.objects.all()
        all_posts = Post.objects.all()
        context["page_user"] = page_user
        context["user_post"] = all_posts
        context["shoes"] = shoes
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



