from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetFrom(forms.ModelForm):
    class Meta:
        model =Tweet
        fields =['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
        #
    class Meta:
        model =User
        fields=('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
        help_texts = {
            'username':None,  # Remove help text for username
            'password1': None,  # Remove help text for password1
            'password2': None,  # Remove help text for password2
        }
        error_messages = {
            'username': {
                'required': 'Username is required.',
            },
            'password1': {
                'required': 'Password is required.',
                'password_mismatch': 'Passwords must match.',
            },
            'password2': {
                'required': 'Password confirmation is required.',
            },
        }

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search Tweets',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search tweets...'})
    )
