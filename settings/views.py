from django.shortcuts import render

# Create your views here.
def getSetting(request):
    return render(request,'organization.html',{'result': 23})