from django.db import models


# Create your models here.
class Student(models.Model): 
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    course = models.CharField(max_length=4, blank=False, null=False)
    gender = models.CharField(max_length=4, blank=False, null=False)
    age = models.IntegerField()
