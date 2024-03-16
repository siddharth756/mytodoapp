from django import forms 
from .models import TodoItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# add listitem form
class AddlistForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Todo','style':'padding:20px'}))
    
    class Meta:
        model = TodoItem
        fields = ['title']

# signup form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username','style':'padding:10px;margin-bottom:10px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password','style':'padding:10px;margin-bottom:10px'}))