from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=50, unique=True)
    emp_name=models.CharField(max_length=100)
    dept=models.CharField(max_length=200)
    #registration_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.emp_name}reg{self.emp_id}'

