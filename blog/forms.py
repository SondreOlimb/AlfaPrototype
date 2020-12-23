from django import forms
from .models import Post,Shoe





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =("title", "title_tag", "author","shoes","strava","lat","lng","header_image","header_image_url","snippet","body","polyline")

        widgets ={
            'title': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title"}),
            'title_tag': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title tag"}),
            'author': forms.TextInput(attrs={"class": "form-control", "value": "","id":"user","type":"hidden"}),
            #'author': forms.Select(attrs={"class": "form-control"}),
            'shoes': forms.CheckboxSelectMultiple(),
            #'body': forms.Textarea(attrs={"class": "form-control","placeholder":"Write your blog post hear"}),
            'header_image_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title tag"}),
            'snippet': forms.Textarea(attrs={"class": "form-control", "placeholder": "Write short introduction"}),
            'strava': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add strava activity number"}),
            'lat': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'lng': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'polyline': forms.TextInput(attrs={"class": "form-control", "value": "", "id": "user", "type": "hidden"}),


        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for AddShoe in self.fields:
                self.fields[AddShoe].widget.attrs['class'] = 'form-control'


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =("title", "title_tag","strava","shoes","lat","lng",'header_image_url',"header_image","snippet","body")

        widgets ={
            'title': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title"}),
            'title_tag': forms.TextInput(attrs={"class": "form-control","placeholder":"Input title tag"}),
            #'author': forms.Select(attrs={"class": "form-control"}),
            'strava': forms.TextInput(attrs={"class": "form-control", "placeholder": "Add strava activity number"}),
            'snippet': forms.Textarea(attrs={"class": "form-control", "placeholder": "Write short introduction"}),
            #'body': forms.Textarea(attrs={"class": "form-control","placeholder":"Write your blog post hear"}),
            'lat': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'lng': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Add latitude coordinates of destination"}),
            'shoes': forms.CheckboxSelectMultiple(),
            'header_image_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title tag"}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for AddShoe in self.fields:
                self.fields[AddShoe].widget.attrs['class'] = 'form-control'




