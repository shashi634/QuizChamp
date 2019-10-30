from django.shortcuts import render

# Create your views here.
def getUsers(request):
    return render(request,'users.html',{'result': 23})