from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.chatbot, name='chatbot'),
    path('chatbot/talk', views.external, name='blog-talk'),
]
