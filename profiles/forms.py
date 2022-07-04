from django import forms
from profiles.models import Profile
from django.contrib.auth.forms import UserCreationForm

class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__" 












