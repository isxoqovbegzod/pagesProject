from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    """ bu view korsatadi """
    template_name = 'home.html'


class AboutsPageView(TemplateView):
    """bu userga Abouts pagesini korsatadi"""
    template_name = "about_us.html"


class Cantact_usView(TemplateView):
    """contact_us ga jovop qaytaruvchi jovop klass"""
    template_name = 'cantact_us.html'