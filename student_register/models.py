from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Reg_no = models.CharField(max_length=50)
    Mobile_no = models.IntegerField(null=False)
    Student_email = models.EmailField(max_length=20)
    Intake_year = models.DateField(auto_now=False)

class Hostel(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Student_stay = models.BooleanField(default=False)
    Members_in_room = models.IntegerField(null=False)

    
    

 
    
    




 
    
    



