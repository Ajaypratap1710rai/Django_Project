# blog/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Post

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            raise forms.ValidationError("Passwords do not match.")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
