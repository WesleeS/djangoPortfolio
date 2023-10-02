from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
class ResumePageView(TemplateView):
    template_name = "resume.html"
class ProjectsPageView(TemplateView):
    template_name = "projects.html"