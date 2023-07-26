from django.db import models
from student_register.models import Student

class Finance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Total_fee = models.IntegerField()
    Fee_paid = models.IntegerField()
    Fee_balance = models.IntegerField() 
