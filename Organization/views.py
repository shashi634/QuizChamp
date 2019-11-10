from django.shortcuts import render
from user.models import User
from .models import Organization, OrganizationLogo
from django.core import serializers
from DjangoLearning.common import currentLoggedInUserData
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from Organization.forms import DocumentForm
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

def organizationLogoUpdate(request):
    try:
        if request.method == 'POST':
            # logo = request.FILES['organizationLogo']
            # fs = FileSystemStorage(location="../OrgLogo")
            # filename = fs.save(logo.name, logo)
            # uploaded_file_url = fs.url(filename)
            form = Document(docfile = request.FILES['docfile'])
            form.save()
            # form.OrgannizationId = Organization.objects.get(id=1)
            # form.PublicId = '8ae8b42f-323b-4f30-aed3-9b71b02c674f'
            # form.LogoUrl = 'shashi.jpg'
            # form.save()
            # if form.is_valid():
            #     form.save()
                # logo = request.FILES['organizationLogo']
                # organizationReference = Organization.objects.get(id=1)
                # organizationLogoData = OrganizationLogo(OrganizationId=organizationReference,PublicId='8ae8b42f-323b-4f30-aed3-9b71b02c674f',LogoUrl=logo.name)
                
                # organizationLogoData.save()
            messages.success(request, form)
            return HttpResponseRedirect('/organization')
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/organization')