from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'blog.html'
    #ordering = ["-id"]
    ordering = ["-post_date"]


# Create your views here.
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

def landing(request):
    return render(request, "landing.html",{})

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = '__all__' #This would post all the fields,
    #fields =("title","body") #we can render spesific fields this way
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    #fields = ["title","title_tag","body"]

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("blog")
