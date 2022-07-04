from django.urls import path
from profiles.views import edit_profile, profile_view


urlpatterns = [
    path("",profile_view.as_view(),name = "profile"),
    path("edit_profile/<slug:pk>/",edit_profile.as_view(),name = "edit_profile"),
] 