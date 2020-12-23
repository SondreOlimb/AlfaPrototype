'''
from django import forms
from .models import Post,Category,AddShoe

shoes = AddShoe.objects.all().values_list("shoe_name","shoe_name")

shoes_list=[]

for item in shoes:
    shoes_list.append(item)

choices =Category.objects.all().values_list("name","name")

choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =("title", "title_tag", "author","category","shoes","strava","lat","lng","header_image","header_image_url","snippet","body","polyline")

        widgets ={
            'title': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title"}),
            'title_tag': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title tag"}),
            'author': forms.TextInput(attrs={"class": "form-control", "value": "","id":"user","type":"hidden"}),
            #'author': forms.Select(attrs={"class": "form-control"}),
            'category': forms.Select(choices = choice_list, attrs={"class": "form-control"}),
            'shoes': forms.Select(choices=shoes_list, attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control","placeholder":"Write your blog post hear"}),
            'header_image_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title tag"}),
            'snippet': forms.Textarea(attrs={"class": "form-control", "placeholder": "Write short introduction"}),
            'strava': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add strava activity number"}),
            'lat': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'lng': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'polyline': forms.TextInput(attrs={"class": "form-control", "value": "", "id": "user", "type": "hidden"}),


        }

        #CheckboxInput


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =("title", "title_tag","strava","shoes","lat","lng",'header_image_url',"header_image","snippet","body")

        widgets ={
            'title': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title"}),
            'title_tag': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title tag"}),
            #'author': forms.Select(attrs={"class": "form-control"}),
            'strava': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add strava activity number"}),
            'snippet': forms.Textarea(attrs={"class": "form-control", "placeholder": "Write short introduction"}),
            'body': forms.Textarea(attrs={"class": "form-control","placeholder":"Write your blog post hear"}),
            'lat': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'lng': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'shoes': forms.Select(choices=shoes_list, attrs={"class": "form-control"}),
            'header_image_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title tag"}),


        }


'''

