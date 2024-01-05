from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.name
    
class Branch(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length = 250)
    DOB = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=[('male','Male'),('female','Female'),('other','Other')])
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account = models.CharField(max_length=20, choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    credit_card = models.BooleanField("Credit Card",default=False)
    debit_card = models.BooleanField("Debit Card",default=False)
    cheque = models.BooleanField("Cheque Book",default=False)
    
    def __str__(self):
        return self.name
    
