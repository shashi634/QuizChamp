from django.urls import path
from . import views

urlpatterns = [
    path('', views.getLoginScreen,name="default"),
    path('registration', views.registration,name="registration"),
    path('admin', views.getUser,name="user"),
    path('add', views.add,name="add"),
    path('userLogin', views.userLogin,name="userLogin"),
    path('registerUser', views.registerUser,name="dashboard"),
]