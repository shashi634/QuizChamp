from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Questions, Options
# Create your views here.
def getQuestions(request):
    return render(request,'Questions.html',{'result': 23})

def addQuestions(request):
    if  request.method == 'POST':
        try:
            organizationName = request.POST['organizationName']

        except Exception as e:
            messages.error(request, e)
            return HttpResponseRedirect('/organization')