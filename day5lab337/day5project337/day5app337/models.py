from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): 
        return self.name
class Employee(models.Model):
        name = models.CharField(max_length=200,) 
        designation = models.CharField(max_length=200,) 
        email=models.EmailField(blank=True) 
        joining_date = models.DateField(auto_now_add=True) 
        salary = models.FloatField(blank=True, null=True,validators=[MinValueValidator(20000), MaxValueValidator(10000000)]) 
        department = models.ForeignKey(Department, blank=True, null=True,on_delete=models.CASCADE)
        def __str__(self):
            return self.name