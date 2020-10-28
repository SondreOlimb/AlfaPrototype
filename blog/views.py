from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

choices =Category.objects.all().values_list("name","name")

choice_list=[]

for item in choices:
    choice_list.append(item)

choice_list = choice_list[1]


class HomeView(ListView):
    model = Post
    template_name = 'blog.html'
    #ordering = ["-id"]
    ordering = ["-post_date"]
    cats = Category.objects.all()

    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context



# Create your views here.
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

def landing(request):
    return render(request, "landing.html",{})

def google(request):
    return render(request, "google.html",{})

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = '__all__' #This would post all the fields,
    #fields =("title","body") #we can render spesific fields this way

class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = "__all__"
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    #fields = ["title","title_tag","body"]

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("blog")

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats.replace("-"," "))

    return render(request, "categories.html", {"cats":cats.title().replace("-"," "),"category_posts":category_posts}) #cats:cats passes the cats to the webpage



