from ast import Not
from calendar import c
import email
from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class company_models(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    logo = models.ImageField(max_length=100)
    email=models.EmailField(max_length=200 )
    password = models.CharField(max_length=100)
    re_enter_password = models.CharField(max_length=100)
    mobile_number = PhoneNumberField()
    company_name = models.CharField(max_length=200)
    company_address = models.TextField()
    interest_rate_followed=models.IntegerField()
    def __str__(self):
        return self.name

class customer_models(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile_number = PhoneNumberField()
    date= models.DateField(auto_now_add=True)
    photo = models.ImageField(max_length=100)
    area_code = models.ForeignKey('finb.areas_models',on_delete=models.CASCADE)
    customer_address = models.TextField()  

class areas_models(models.Model):
    id = models.IntegerField(primary_key=True)
    area_code = models.CharField(max_length=50,unique=True)  
    area_name = models.CharField(max_length=200 )

class accounts_models(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey('finb.customer_models', on_delete=models.CASCADE)
    lone_amount = models.FloatField()
    area_code = models.ForeignKey('finb.areas_models',on_delete=models.CASCADE)
    lone_issue_date = models.DateTimeField(auto_now_add=True)
    daily_debt = models.IntegerField()
    number_of_days = models.IntegerField()
    paid_amount = models.FloatField( default=0)
    debt_amount = models.FloatField()
    interest= models.IntegerField( default=0)
    is_debt_closed = models.BooleanField(default=False)

