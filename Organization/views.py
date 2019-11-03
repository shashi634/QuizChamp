from django.shortcuts import render
from user.models import User
from .models import Organization
from django.core import serializers
from DjangoLearning.common import currentLoggedInUserData
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def getUser(request):
    currentLoggedInUserDetails = request.session["quizChampAdmin"].split('~')
    organizationData = Organization.objects.get(PublicId=currentLoggedInUserDetails[2])
    return render(request,'home.html' , {'organization': organizationData, 'userName':currentLoggedInUserDetails[0]})

def organizationDetailsUpdate(request):
    try:
        if request.method == 'POST':
            organizationName = request.POST['organizationName']
            organizationDescription = request.POST['organizationDescription']
            if not organizationName:
                messages.error(request,"Organization Name can't be blank!")
                return HttpResponseRedirect('/organization')
            currentLoggedInUserDetails = request.session["quizChampAdmin"].split('~')
            organizationData = Organization.objects.get(PublicId=currentLoggedInUserDetails[2])
            organizationData.Name = organizationName
            organizationData.Description = organizationDescription
            organizationData.save()
            messages.success(request,"Data Saved Successfully!")
            return HttpResponseRedirect('/organization')
    except Exception as e:
        messages.error(request, "Something went wrong!")
        return HttpResponseRedirect('/organization')