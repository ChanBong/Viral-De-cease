from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('chatbot/', views.chatbot, name='blog-bot'),
    path('chatbot/talk', views.external, name='blog-talk'),
]
