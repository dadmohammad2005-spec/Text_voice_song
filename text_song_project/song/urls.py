from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-audio/', views.generate_audio, name='generate_audio'),
]