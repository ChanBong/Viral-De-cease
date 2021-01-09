from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='about'),
    path('covid/', views.covid, name='covid'),
    path('aids/', views.aids, name='aids'),
    path('rabies/', views.rabies, name='rabies'),
    path('diseas_library/', views.diseas_library, name='diseas_library'),
]
