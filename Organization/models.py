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
    LogoUrl = models.ImageField(upload_to='OrgLogo')