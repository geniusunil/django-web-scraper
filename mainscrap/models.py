from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=40,blank=False)
    csv_file = models.FileField(upload_to='documents/',blank=False)

    def __str__(self):
        return self.filename
