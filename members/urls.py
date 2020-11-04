
from django.urls import path
from .views import UserRegisterView, UserEditView,PasswordsChangeView, ShowProfilePageView
from django.contrib.auth import views as auth_views
from . import views






urlpatterns = [
    path("register/",UserRegisterView.as_view(),name="register"),
    path("edit_profile/",UserEditView.as_view(),name="user_edit"),
    #path("password/",auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"),name="change-password"),
    path("password/",PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    path("password_success/",views.password_success,name="password_success"),
    path("<int:pk>/profile",ShowProfilePageView.as_view(),name="show_profile_page")

]
