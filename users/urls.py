from django.urls import path
from . import views

urlpatterns = [
    path('allUsers', views.getUsers, name="default"),
]