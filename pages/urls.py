from django.urls import path
from .views import HomePageView, ResumePageView, ProjectsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("resume/", ResumePageView.as_view(), name="resume"),
    path("projects/", ProjectsPageView.as_view(), name="projects"),
]