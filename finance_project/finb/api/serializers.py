from asyncore import read
from operator import is_
from re import M
from tkinter import E
from finb.models import *
from rest_framework import serializers
class company_serializer(serializers.ModelSerializer):
    class Meta:
        model = company_models
        fields = '__all__' #['id', 'name', 'email','customer_models' ,'password', 're_enter_password', 'mobile_number','company_name','company_address','interest_rate_followed']
    #
    # def validate(self ,data):
    #     fields = ['name','mobile_number','photo','area_code','customer_address','models']
    def validate(self,data):
        if data['password']!=data['re_enter_password']:
            raise serializers.ValidationError('both password and re_enter_password should be same')
        else:
            return data


class areas_serializer(serializers.ModelSerializer):
    class Meta:
        model = areas_models
        fields = '__all__'
    def validate_area_code(self,value):
        if len(value) >4:
            raise serializers.ValidationError("Area code too long")
        else:
            return value


class accounts_serializer(serializers.ModelSerializer):
    class Meta:
        model = accounts_models
        fields = "__all__"
    def validate(self, data):
        if data['debt_amount']!= 0:
            return data['is_debt_closed']==False and data
        else:
            return data['is_debt_closed']==True and data



class customer_serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_models
        fields = '__all__'
