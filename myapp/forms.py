from django.forms import fields
from django.forms import widgets
from .models import Post,Profile
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titles','desc']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','id':'myusername'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'})
        }
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pro_pic','bio','dob','prof','qualif']
        widgets ={
            'pro_pic':forms.FileInput(attrs={'class':'form-control-file'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'prof':forms.TextInput(attrs={'class':'form-control'}),
            'qualif': forms.TextInput(attrs={'class': 'form-control'}),
        }
