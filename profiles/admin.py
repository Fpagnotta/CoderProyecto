from django.contrib import admin
from profiles.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin (admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','user','email']

