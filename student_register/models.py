from django.db import models

# Create your models here.
 
class Student( models.Model) :
    Name = models.CharField(max_length=100)
    Reg_no=models.CharField(max_length=50)
    Mobile_no=models.IntegerField
    Student_email=models.EmailField(max_length=20)


class Hostel (models.Model):
    Student_stay =models.BooleanField(default=False)

 
    
    



