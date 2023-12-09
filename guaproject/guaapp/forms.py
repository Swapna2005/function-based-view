from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput())
