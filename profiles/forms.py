from django import forms
from profiles.models import Profile


class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__" 