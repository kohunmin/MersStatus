from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class mersStatus(models.Model):
    user = models.ForeignKey(User);
    coughStatus = models.CharField(max_length=100)
    breathingStatus = models.CharField(max_length=100)
    temperature = models.FloatField(max_length=10)
    pub_date = models.DateTimeField()
