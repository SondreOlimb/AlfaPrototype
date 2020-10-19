from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255, default='Go Explore')
    author =models.ForeignKey(User, on_delete=models.CASCADE)  #this line deletes all elements created by this user if this user is deleted
    body = models.TextField()


    def __str__(self):
        return self.title + ' | ' + str(self.author) #lets us se the title o the blog page in the admin page

