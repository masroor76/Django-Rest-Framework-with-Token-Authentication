from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=100, default='StudentName')
    RollNumber = models.IntegerField(default= 0)
    CityName = models.CharField(max_length=100, default='StudentCityName')

    def __str__(self):
        return self.Name