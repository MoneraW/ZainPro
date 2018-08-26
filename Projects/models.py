from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    projectname = models.CharField(max_length=120)
    projectowner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    duedate = models.TimeFields()
    status = models.CharField()
    description = models.CharField(max_length=250)
    