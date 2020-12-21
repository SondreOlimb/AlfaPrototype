from django.db import models
from django.urls import reverse
from datetime import datetime,date
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name  # lets us se the title o the blog page in the admin page


    def get_absolute_url(self):
        return reverse("landing")  # this element loads the post after publishing
        # return reverse("blog")  #if we want to jump to return after

class AddShoe(models.Model):
    shoe_name = models.CharField(max_length=255)
    link_picture =models.CharField(max_length=255)
    link_shoe = models.CharField(max_length=255,default=0)


    def __str__(self):
        return self.shoe_name  # lets us se the title o the blog page in the admin page


    def get_absolute_url(self):
        return reverse("landing")  # this element loads the post after publishing
        # return reverse("blog")  #if we want to jump to return after


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255)
    author =models.ForeignKey(User, on_delete=models.CASCADE)  #this line deletes all elements created by this user if this user is deleted
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    body =RichTextField(blank=True,null=True)
    snippet = models.CharField(max_length=255)
    #body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    shoes = models.CharField(max_length=255, default="0")
    likes = models.ManyToManyField(User,related_name="blog_posts")
    strava =models.IntegerField(default=0)
    lat = models.DecimalField(max_digits=10, decimal_places=8,default=0)
    lng = models.DecimalField(max_digits=11, decimal_places=8,default=0)
    polyline = models.CharField(max_length=100000, default=0)




    def total_likes(self):
        return self.likes.count()



    def __str__(self):
        return self.title + ' | ' + str(self.author) #lets us se the title o the blog page in the admin page

    def get_absolute_url(self):
        return reverse("article-detail", args=[str(self.id)]) #this element loads the post after publishing
        #return reverse("blog")  #if we want to jump to return after

class Profile(models.Model):
    user =models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.CharField(null=True, blank=True, max_length=255)
    facebook_url = models.CharField(null=True, blank=True, max_length=255)
    twitter_url = models.CharField(null=True, blank=True, max_length=255)
    instagram_url = models.CharField(null=True, blank=True,max_length=255)
    pintrest_url = models.CharField(null=True, blank=True,max_length=255)
    shoes = models.ManyToManyField(AddShoe)



    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("show_profile_page", args=[str(self.id)])