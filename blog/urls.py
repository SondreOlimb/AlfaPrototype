
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView




urlpatterns = [
    #path('', views.home,name="home"),
    path("blog",HomeView.as_view(),name="blog"),
    path('article/<int:pk>' ,ArticleDetailView.as_view(),name="article-detail") , #pk is the primary key, its atoganerated by the database. in means that its a integer
    path("",views.landing,name="landing"),
]
