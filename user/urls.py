from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin,name="default"),
    path('registration', views.registration,name="registration"),
    path('userLogin', views.userLogin,name="Dashboard"),
    path('logOut', views.logOut,name="Dashboard"),
]