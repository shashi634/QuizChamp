from django.db import models
import uuid

# Create your models here.
class Subject(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Name = models.CharField(max_length=100)

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    PublicId = models.UUIDField(default=uuid.uuid4)
    Question = models.TextField()
    CreatedDate = models.DateTimeField()
    CreatedBy = models.UUIDField(default=uuid.uuid4)
    LastUpdatedDate = models.DateTimeField()
    LastUpdatedBy = models.UUIDField(default=uuid.uuid4)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Options(models.Model):
    id = models.AutoField(primary_key=True)
    PublicId = models.UUIDField(default=uuid.uuid4)
    Question = models.ForeignKey(Subject, on_delete=models.CASCADE)
    OptionsA = models.TextField()
    OptionsB = models.TextField()
    OptionsC = models.TextField()
    OptionsD = models.TextField()
    CorrectiOption = models.TextField()
    IsMultipleOption = models.BooleanField(default=False)
    CreatedDate = models.DateTimeField()
    CreatedBy = models.UUIDField(default=uuid.uuid4)
    LastUpdatedDate = models.DateTimeField()
    LastUpdatedBy = models.UUIDField(default=uuid.uuid4)
