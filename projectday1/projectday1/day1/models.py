from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    present_address=models.CharField(max_length=200)
    registration_date=models.DateTimeField(auto_now_add=True)
    reg_no=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.name}reg{self.reg_no}'


