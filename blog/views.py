from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from myBlog.settings import MAPBOX_KEY


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

    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        fetch_likes = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = fetch_likes.total_likes()

        liked = False
        if fetch_likes.likes.filter(id=self.request.user.id).exists():
            liked = True


        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["mapbox_access_token"] = MAPBOX_KEY
        context["liked"]=liked
        return context

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
    ordering = ["-category_posts.post_date"]

    return render(request, "categories.html", {"cats":cats.title().replace("-"," "),"category_posts":category_posts}) #cats:cats passes the cats to the webpage

def LikeView(request,pk):

    post = Post.objects.get(id=pk)

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked =True

    return HttpResponseRedirect(reverse("article-detail",args=[str(pk)]))





