from django.db import models
import uuid

# Create your models here.
class Subject(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Name = models.CharField(max_length=100)