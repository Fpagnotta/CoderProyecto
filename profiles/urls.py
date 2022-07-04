from django.urls import path
from profiles.views import edit_profile, profile_view,create_profile
from tu_vehiculo.views import index, login_view, logout_view, about_us


urlpatterns = [
    path("",profile_view.as_view(),name = "profile"),
    path('signup/',create_profile.as_view(),name = "signup"),
    path("profile/<int:pk>",profile_view.as_view(),name = "update_profile"),
    path("edit_profile/<int:pk>/",edit_profile.as_view(),name = "edit_profile"),
   
] 