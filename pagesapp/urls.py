from django.urls import path
from .views import HomePageView, AboutsPageView, Cantact_usView

urlpatterns = [
    path('about_us/', AboutsPageView.as_view(), name='about_us'),
    path('', HomePageView.as_view(), name='home'),
]







