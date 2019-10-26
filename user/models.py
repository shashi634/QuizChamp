from django.db import models
from Organization.models import Organization
# Create your models here.

class User(models.Model):
    UserName = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 500)
    EmailId = models.EmailField(max_length = 254,blank = True, null = False, unique = True)
    IsActived = models.BooleanField(default = False)
    ActivatiedOn = models.DateTimeField(default = None, editable = True)
    OrganizationId = models.ForeignKey(Organization, on_delete=models.CASCADE)
    #OrganizationId = models.OneToOneField("Organization.Organization", on_delete=models.CASCADE)
