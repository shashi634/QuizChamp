from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from  Organization.models import Organization 
import hashlib, binascii, os
import datetime
#from DjangoLearning.common import hashPassword
# Create your views here.
def getUser(request):
    # insted of this we are going to use templates
    # return HttpResponse("shashi shanker singh")
    userData = User.objects.get(id=1)
    return render(request,'home.html' , {'userName': userData.EmailId})

def add(request):
    number1 = int(request.POST['num1'])
    number2 = int(request.POST['num2'])
    number3 = number1 + number2
    return render(request,'result.html',{'result': number3})

def getLoginScreen(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def userLogin(request):
    return render(request,'registration.html')

def registerUser(request):
    userName = str(request.POST['userName'])
    password = str(request.POST['password'])
    emailId = str(request.POST['emailId'])
    organization = Organization.objects.get(id=1)
    user = User()
    user.UserName = userName
    user.Password = password
    user.EmailId = emailId
    user.IsActived = True
    user.ActivatiedOn = datetime.datetime.now()
    user.OrganizationId = organization
    user.save()
    return render(request,'result.html')

def newMethod():
    