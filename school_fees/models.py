from django.db import models
from student_register.models import Student

class Finance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,default = 0)
    Total_fee = models.IntegerField(default = 0)
    Fee_paid = models.IntegerField(default = 0)
    Fee_balance = models.IntegerField(default = 0) 
