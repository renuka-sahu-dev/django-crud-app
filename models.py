from django.db import models

# Create your models here.


class signup(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  password=models.CharField(max_length=235)
  gender=models.CharField(max_length=10)