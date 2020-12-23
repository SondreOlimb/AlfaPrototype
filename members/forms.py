from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from blog.models import Profile
from django import forms
from blog.models import Profile, Shoe

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ("bio", "profile_pic", "website_url", "facebook_url", "twitter_url", "instagram_url", "pintrest_url")

        widgets = {
            'website_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'facebook_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'twitter_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'instagram_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'pintrest_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write short bio"}),
            #"profile_pic": forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"})
        }

class EditProfilePageForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields= ("bio", "profile_pic", "website_url", "facebook_url", "twitter_url", "instagram_url", "pintrest_url","shoes")

        widgets ={
            'website_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'facebook_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'twitter_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'instagram_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            'pintrest_url': forms.TextInput(attrs={"class": "form-control", "placeholder": "Input title"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write short bio"}),
            'shoes': forms.CheckboxSelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for AddShoe in self.fields:
                self.fields[AddShoe].widget.attrs['class'] = 'form-control'






class SignUpForms(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder":"Input email"}))
    first_name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={"class": "form-control","placeholder":"Input first name"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Input last name"}))

    class Meta:
            model =User
            fields =("username","first_name","last_name","email","password1","password2")
    def __init__(self,*args,**kwargs):
        super(SignUpForms,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs['class']='form-control'
        self.fields["password1"].widget.attrs['class']='form-control'
        self.fields["password2"].widget.attrs['class']='form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder":"Input email"}))
    first_name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={"class": "form-control","placeholder":"Input first name"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Input last name"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Input last name"}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Input last name"}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check", "placeholder": "Input last name"}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check", "placeholder": "Input last name"}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check", "placeholder": "Input last name"}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Input last name"}))


    class Meta:
            model =User
            fields =("username","first_name","last_name","email","last_login","is_superuser","is_staff","is_active","date_joined")


class PasswordChangeingForms(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type":"password"}))
    new_password1= forms.CharField(max_length=100,widget= forms.PasswordInput(attrs={"class": "form-control","type":"password"}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class": "form-control","type":"password"}))

    class Meta:
            model =User
            fields =("old_password","new_password1","new_password2")