from django.db import models


class User(models.Model):
    user_name   = models.CharField(max_length=50)
    first_name  = models.CharField(max_length=50,blank=False)
    last_name   = models.CharField(max_length=50,blank=False)
    email       = models.EmailField(max_length=70,blank=True)
    password    = models.CharField(max_length=12,blank=False)

    def __str__(self):
        return self.first_name
