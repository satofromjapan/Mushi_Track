from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tracker_home'),
    path('about', views.about, name='tracker_about')
]