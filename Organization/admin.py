from django.contrib import admin
from .models import Organization, OrganizationLogo
# Register your models here.

admin.site.register(Organization)
admin.site.register(OrganizationLogo)