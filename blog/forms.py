from django import forms
from .models import Post,Category

choices =Category.objects.all().values_list("name","name")

choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =("title", "title_tag", "author","category","body")

        widgets ={
            'title': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title"}),
            'title_tag': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title tag"}),
            'author': forms.TextInput(attrs={"class": "form-control", "value": "","id":"user","type":"hidden"}),
            #'author': forms.Select(attrs={"class": "form-control"}),
            'category': forms.Select(choices = choice_list, attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control","placeholder":"Write your blog post hear"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =("title", "title_tag","body")

        widgets ={
            'title': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title"}),
            'title_tag': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title tag"}),
            #'author': forms.Select(attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control","placeholder":"Write your blog post hear"}),
        }




