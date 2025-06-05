from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='homePage'),
    path('contact-us', views.contactView, name='contactPage')
]