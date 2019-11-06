from django.db import models

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=30,default='')
    symptoms = models.TextField(default='')
    precautions = models.TextField(default='')
    doctors = models.TextField(default='')

    def __str__(self):
        return self.name


