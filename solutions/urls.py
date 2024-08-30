from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("solutions", views.solutions, name="solutions"),
    path("solutions/<int:id>", views.solutionsdetails, name="details"),
    path("about", views.about, name="about"),
    path("policies", views.policies, name="policies"),
    path("missionAndVision", views.missionAndVision, name="missionAndVision"),
    
]
