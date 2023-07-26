from django.db import models

# Create your models here.
class NormalUserModel(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=12)
    pass1 = models.CharField(max_length=40)
    pass2 = models.CharField(max_length=40)