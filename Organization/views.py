from django.shortcuts import render
from user.models import User
# Create your views here.
def getUser(request):
    userData = User.objects.get(id=1)
    return render(request,'home.html' , {'userName': userData.UserName})