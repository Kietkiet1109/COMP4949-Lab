# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, kietPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('kiet/', kietPageView, name='kiet'),     # Exercise 1
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
