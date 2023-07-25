from django.db import models

# Create your models here.
class Finance(models.Model):
    Total_fee = models.IntegerField
    Fee_balance = models.IntegerField
    Fee_paid = models.IntegerField
    