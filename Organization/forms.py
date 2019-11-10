from django import forms
from Organization.models import OrganizationLogo

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    