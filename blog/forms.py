from django import forms
from .models import Post,Shoe



class ShoeForm(forms.ModelForm):

    class Meta:
        valg = [("20", 20), ("40", 40), ("60", 60), ("80", 80), ("100", 100)]
        model = Shoe
        fields = ("shoe_name","link_picture","link_shoe","water_resistance","breathability","sole_stiffness","isolation","ankle_stabilization")
        widgets ={
                'shoe_name' : forms.TextInput(attrs={"class": "form-control","placeholder":"Input shoe name"}),
                'link_picture': forms.TextInput(attrs={"class": "form-control","placeholder":"Input link to shoe picture"}),
                'link_shoe' : forms.TextInput(attrs={"class": "form-control","placeholder":"Input title"}),
                'water_resistance': forms.Select(choices=valg,attrs={'class': 'form-control'}),
                'breathability': forms.Select(choices=valg,attrs={'class': 'form-control'}),
                'sole_stiffness': forms.Select(choices=valg,attrs={'class': 'form-control'}),
                'isolation': forms.Select(choices=valg,attrs={'class': 'form-control'}),
                'ankle_stabilization': forms.Select(choices=valg ,attrs={'class': 'form-control'}),
        }


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




