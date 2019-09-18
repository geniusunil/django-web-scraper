from django.db import models



class Data(models.Model):
    username = models.CharField(max_length=40)
    csv_file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.username    
