from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Profile,Shoe
from .forms import PostForm, EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from myBlog.settings import MAPBOX_KEY ,STRAVA_CLIENT_ID,STRAVA_CLIENT_SECRET,STRAVA_REFRESH_TOKEN

import requests
import urllib3
import polyline
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)






class TripMapView(ListView):
    model = Post
    template_name = "trip_map.html"
    all_posts = Post.objects.all()
    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data

        context = super(TripMapView, self).get_context_data(*args, **kwargs)
        all_posts = Post.objects.all()
        context["all_post"] = all_posts
        context["mapbox_access_token"] = MAPBOX_KEY

        return context

class AddshoeView(CreateView):
    model = Shoe
    template_name = "add_shoe.html"
    fields = "__all__"



#choices =Category.objects.all().values_list("name","name")

#choice_list=[]

#for item in choices:
 #   choice_list.append(item)

#choice_list = choice_list[1]


class HomeView(ListView):
    model = Post
    template_name = 'blog.html'
    #ordering = ["-id"]
    ordering = ["-post_date"]
    #cats = Category.objects.all()

    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data
        #cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        #context["cat_menu"] = cat_menu
        return context



# Create your views here.
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data
        #cat_menu = Category.objects.all()
        shoes = Shoe.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        fetch_likes = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = fetch_likes.total_likes()

        liked = False
        if fetch_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

         #only fetches the strava api the first time the blog is visited, after that it is saved in the database
        if fetch_likes.strava and fetch_likes.polyline == str(0):
            auth_url = "https://www.strava.com/oauth/token"
            # activites_url = "https://www.strava.com/api/v3/athlete/activities/{4056947490}"
            activites_url = "https://www.strava.com/api/v3/activities/" +str(fetch_likes.strava)

            payload = {
                'client_id': STRAVA_CLIENT_ID,
                'client_secret': STRAVA_CLIENT_SECRET,
                'refresh_token': STRAVA_REFRESH_TOKEN,
                'grant_type': "refresh_token",
                'f': 'json'
            }

            res = requests.post(auth_url, data=payload, verify=False)
            access_token = res.json()["access_token"]

            header = {'Authorization': 'Bearer ' + access_token}
            param = {'per_page': 2, 'page': 1}
            my_dataset = requests.get(activites_url, headers=header, params=param).json()
            strava_tempsave = my_dataset["map"]["polyline"]
            path = polyline.decode(strava_tempsave, geojson=True)
            fetch_likes.polyline = strava_tempsave
            fetch_likes.save()
            poly = []
            for i in path:
                poly.append([i[0], i[1]])

            context["poly"] = poly

        elif fetch_likes.polyline != str(0):
            path = polyline.decode(fetch_likes.polyline, geojson=True)
            poly = []
            for i in path:
                poly.append([i[0], i[1]])

            context["poly"] = poly


        #context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["mapbox_access_token"] = MAPBOX_KEY
        context["liked"]=liked
        context["shoes"] = shoes
        return context








class LandingView(ListView):
    model = Profile
    template_name = "landing.html"

    def get_context_data(self, *args, **kwargs): #this needs to bee aded to evry view that wants the category data

        context = super(LandingView, self).get_context_data(*args, **kwargs)
        all_profiles = Profile.objects.all()
        context["all_profiles"] = all_profiles
        return context





class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = '__all__' #This would post all the fields,
    #fields =("title","body") #we can render spesific fields this way

#class AddCategoryView(CreateView):
 #   model = Category
  #  template_name = "add_category.html"
   # fields = "__all__"
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    #fields = ["title","title_tag","body"]

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("blog")

#def CategoryView(request,cats):
#    category_posts = Post.objects.filter(category=cats.replace("-"," "))
#   ordering = ["-category_posts.post_date"]

#    return render(request, "categories.html", {"cats":cats.title().replace("-"," "),"category_posts":category_posts}) #cats:cats passes the cats to the webpage

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








