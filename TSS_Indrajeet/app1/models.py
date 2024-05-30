from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Photo=models.URLField()
    Password=models.CharField(max_length=20)

    def __str__(self):
        return self.Name
 
 