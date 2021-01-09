from django.urls import path
from . import views
from .views import (
    DiseasListView,
)

urlpatterns = [
    path('', DiseasListView.as_view(), name='diseas-home'),
]
