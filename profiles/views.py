from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView
from profiles.models import Profile 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class profile_view(ListView):
    model = Profile
    template_name = "profile.html"
    queryset: Profile.objects.filter


class detail_profile_view(DetailView):
    model = Profile
    template_name = "profile_details.html"
    fields = "__all__"

class edit_profile(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = "edit_profile.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("index", kwargs= {"pk": self.object.pk})