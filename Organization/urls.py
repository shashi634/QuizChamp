from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUser,name="user"),
    path('update', views.organizationDetailsUpdate,name="update"),
    path('orgLogoUpdate', views.organizationLogoUpdate,name="orgLogoUpdate"),
]