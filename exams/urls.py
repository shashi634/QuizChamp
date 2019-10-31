from django.urls import path
from . import views

urlpatterns = [
    path('', views.getExams, name="default"),
]