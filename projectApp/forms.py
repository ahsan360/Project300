from django import forms
 
from django.contrib.auth.models import User
from . models import Add
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1' ,'password2']

class GeeksForm(forms.ModelForm):
    
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Add
  
        # specify fields to be used
        fields = ['title', 'author',  'body']
  
        widget = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control'}),
       }