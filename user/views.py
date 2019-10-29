from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from  Organization.models import Organization 
import hashlib, binascii, os
import datetime
from django.contrib import messages
from DjangoLearning.common import checkEmail
from django.http import HttpResponseRedirect
#from DjangoLearning.common import hashPassword
# Create your views here.
def getUser(request):
    # insted of this we are going to use templates
    # return HttpResponse("shashi shanker singh")
    userData = User.objects.get(id=1)
    return render(request,'home.html' , {'userName': userData.UserName})

def add(request):
    number1 = int(request.POST['num1'])
    number2 = int(request.POST['num2'])
    number3 = number1 + number2
    return render(request,'result.html',{'result': number3})

def userLogin(request):
    try:
        if request.method == "POST":
            emailId = str(request.POST['emailId'])
            password = str(request.POST['password'])
            userInfo = User.objects.get(EmailId = emailId, Password = password)
            #messages.success(request, userInfo.OrganizationId.Name)
            return HttpResponseRedirect('/dashboad')
        else:
            return render(request,'login.html')
    except Exception as e:
        messages.error(request, e.args)
        return render(request,'login.html')
    

def registration(request):
    try:
        # checking if method is Post then go something otherwise no need to do extra.
        if request.method == "POST":
            # getting data from Form
            userName = str(request.POST['userName'])
            password = str(request.POST['password'])
            rePassword = str(request.POST['rePassword'])
            emailId = str(request.POST['emailId'])
            # validation of data
            if userName is None:
                messages.error(request, 'Username must not empty of null!')
                return render(request,'registration.html')
            if password is None:
                messages.error(request, 'Password must not empty of null!')
                return render(request,'registration.html')
            if(checkEmail(emailId) == False):
                messages.error(request, 'Not valid Email!')
                return render(request,'registration.html')
            if(len(password)<8 or len(password)>16):
                messages.error(request, 'Password length should be between 8 and 16.')
                return render(request,'registration.html')
            if not (password == rePassword):
                messages.error(request, 'Password does not matches')
                return render(request,'registration.html')
            # Now Organzation comes in the role as user will be assicated with Organization only
            organizationPublicId = request.GET.get('orgId')
            organization = Organization.objects.get(PublicId=organizationPublicId)
            user = User()
            user.UserName = userName
            user.Password = password
            user.EmailId = emailId
            user.IsActived = True
            user.ActivatiedOn = datetime.datetime.now()
            user.OrganizationId = organization
            user.save()
            messages.success(request, 'Registration successful')
            return render(request,'registration.html')
        else:
            return render(request,'registration.html')
    except Exception as e: 
        messages.error(request, "Something went wrong. PLease try again.")
        return render(request,'registration.html')
    

