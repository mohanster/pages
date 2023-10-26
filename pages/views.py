# Create your views here.
from django.views.generic import TemplateView

class HomePageView (TemplateView):
       template_name = "Home.html"

class AboutPageView (TemplateView): #new
    template_name = "About.html"
    