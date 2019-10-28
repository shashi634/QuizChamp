from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin,name="default"),
    path('registration', views.registration,name="registration"),
    path('dashboad', views.getUser,name="user"),
    path('add', views.add,name="add"),
    path('userLogin', views.userLogin,name="Dashboard"),
]