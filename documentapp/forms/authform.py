from django import forms

class SignupDETAILS(forms.Form):
    first_name=forms.CharField(label="FirstName", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(label="lastname", widget=forms.TextInput(attrs={'class': 'form-control'}))
    username=forms.CharField(label="UserName", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginupDETAILS(forms.Form):
    username=forms.CharField(label="username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class': 'form-control'}))


