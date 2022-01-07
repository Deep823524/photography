from django.db import models


# Create your models here.
class contact_us(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    website = models.CharField(max_length=20)
    message = models.CharField(max_length=200)

