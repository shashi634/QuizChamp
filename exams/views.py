from django.shortcuts import render

# Create your views here.
def getExams(request):
    return render(request,'exams.html',{'result': 23})