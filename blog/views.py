from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blog.html'


# Create your views here.
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

def landing(request):
    return render(request, "landing.html",{})