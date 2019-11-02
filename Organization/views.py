from django.shortcuts import render
from user.models import User
from .models import Organization
from django.core import serializers
from DjangoLearning.common import currentLoggedInUserData
# Create your views here.
def getUser(request):
    currentLoggedInUserDetails = request.session["quizChampAdmin"].split('~')
    organizationData = Organization.objects.get(PublicId=currentLoggedInUserDetails[2])
    return render(request,'home.html' , {'organization': organizationData, 'userName':currentLoggedInUserDetails[0]})