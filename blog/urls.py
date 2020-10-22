
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView,UpdatePostView,DeletePostView




urlpatterns = [
    #path('', views.home,name="home"),
    path("blog",HomeView.as_view(),name="blog"),
    path('article/<int:pk>' ,ArticleDetailView.as_view(),name="article-detail") , #pk is the primary key, its atoganerated by the database. in means that its a integer
    path("",views.landing,name="landing"),
    path('newpost/',AddPostView.as_view(),name="add_post"),
    path("article/<int:pk>/edit/",UpdatePostView.as_view(),name="update_post"),
    path("article/<int:pk>/delete/",DeletePostView.as_view(),name="delete_post")
]
