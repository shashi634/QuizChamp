from django.db import models

# Create your models here.
class Organization(models.Model):
    Name = models.CharField(max_length = 200)
    Description = models.TextField()
    PublicId = models.CharField(max_length=64)
    ActivatedOn = models.DateTimeField(default = None, editable = True)
    ActivatedTill = models.DateTimeField(default = None, editable = True)

class OrganizationLogo(models.Model):
    OrganizationId = models.ForeignKey(Organization, on_delete=models.CASCADE)
    PublicId = models.CharField(max_length=64)
    LogoUrl = models.ImageField(upload_to='OrgLogo/%Y/%m/%d')

class OrganizationAddress(models.Model):
    OrganizationId = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    PinCode = models.CharField(max_length=10)
    Country = models.CharField(max_length=50)
    AddressType = models.SmallIntegerField(default=1)
    IsActive = models.BooleanField(default = True)

class OrganizationContactPerson(models.Model):
    OrganizationId = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)
    Designation = models.CharField(max_length=50)
    WorkingFrom = models.DateTimeField(default = None, editable = True)
    IsActive = models.BooleanField(default = True)
    WorkedTill = models.DateTimeField(default = None, editable = True)
    PostedAt = models.ForeignKey(OrganizationAddress, on_delete=models.CASCADE)