import uuid
from django.db import models

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name