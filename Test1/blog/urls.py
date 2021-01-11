from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='about'),
    path('covid/', views.covid, name='covid'),
    path('aids/', views.aids, name='aids'),
    path('rabies/', views.rabies, name='rabies'),
    path('h1n1/', views.h1n1, name='h1n1'),
    path('commoncold/', views.commoncold, name='commoncold'),
    path('hepatitisa/', views.hepatitisa, name='hepatitisa'),
    path('hepatitisb/', views.hepatitisb, name='hepatitisb'),
    path('diseas_library/', views.diseas_library, name='diseas_library'),
]
