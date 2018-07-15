from documentapp.models import *
from django import forms
from django.forms import Textarea

class ProfileForm(forms.ModelForm):
    class Meta(object):
        model=Profile
        widgets={
            'address':Textarea(attrs={'cols':30,'rows':10}),
        }
        exclude=['user']