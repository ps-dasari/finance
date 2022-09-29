from ast import Not
from calendar import c
from decimal import DefaultContext
import email
from enum import unique
from math import fabs
#from wsgiref.validate import validator
from django.core import validators
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


# Create your models here.
#its a model for company details

class company_models(models.Model):
    #id = models.IntegerField(primary_key=True,serialize=False,auto_created=True)
    name = models.CharField(max_length=200)
    logo = models.ImageField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True,error_messages={'message':'invalid mail id'})
    password = models.CharField(max_length=100)
    re_enter_password = models.CharField(max_length=100)
    mobile_number = PhoneNumberField(null=True,validators=[RegexValidator(r'[9876][0-9]{9}$')])
    company_name = models.CharField(max_length=200,null=True,blank=True)
    company_address = models.TextField(null=True, blank=True)
    interest_rate_followed=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name+str(self.company_name)


#its a model for customer details
class customer_models(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.ForeignKey('finb.accounts_models', on_delete=models.CASCADE)
    mobile_number = models.ForeignKey('finb.accounts_models', on_delete=models.CASCADE,related_name='+')
    date= models.DateField(auto_now_add=True)
    photo = models.ImageField(max_length=100,null=True,blank=True)
    area_code = models.ForeignKey('finb.areas_models',on_delete=models.CASCADE,related_name='customer_models')
    customer_address = models.TextField()
    def __str__(self):
        return str('%s object' % self.__class__.__name__)
#its a model for areas_models
class areas_models(models.Model):
    #id = models.IntegerField(primary_key=True)
    area_code = models.CharField(max_length=10,unique=True)
    area_name = models.CharField(max_length=200 )
    def __str__(self):
        return self.area_code

#its a model for accounts_models
class accounts_models(models.Model):
   # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200) #ForeignKey('finb.customer_models', on_delete=models.CASCADE)
    mobile_number = PhoneNumberField(null=True, validators=[RegexValidator(r'[9876][0-9]{9}$')])
    lone_amount = models.FloatField()
    area_code = models.ForeignKey('finb.areas_models',on_delete=models.CASCADE,related_name='accounts_models')
    lone_issue_date = models.DateTimeField(auto_now_add=True)
    daily_debt = models.IntegerField()
    number_of_days = models.IntegerField()
    paid_amount = models.FloatField( default=0)
    debt_amount = models.FloatField()
    interest= models.IntegerField( default=0)
    is_debt_closed = models.BooleanField(default=False)
    def __str__(self):
        return self.name+str(self.lone_amount)
