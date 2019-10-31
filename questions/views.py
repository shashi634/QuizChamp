from django.shortcuts import render

# Create your views here.
def getQuestions(request):
    return render(request,'Questions.html',{'result': 23})