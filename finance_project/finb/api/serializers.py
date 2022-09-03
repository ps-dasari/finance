from asyncore import read
from re import M
from finb.models import *
from rest_framework import serializers

class company_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    logo=serializers.ImageField()
    email = serializers.CharField()
    password = serializers.CharField()
    re_enter_password = serializers.CharField()
    mobile_number = serializers.IntegerField()
    company_name = serializers.CharField()
    company_address = serializers.CharField()
    interest_rate_followed = serializers.IntegerField()


class customer_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    date= serializers.DateField()
    photo = serializers.ImageField()
    area_code = serializers.CharField()
    customer_address = serializers.CharField()


class areas_serializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    area_code = serializers.CharField()
    area_name = serializers.CharField()

class accounts_serializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    lone_amount = serializers.FloatField()
    area_code = serializers.CharField()
    lone_issue_date = serializers.DateField()
    daily_debt = serializers.IntegerField()
    number_of_days = serializers.IntegerField()
    paid_amount = serializers.FloatField()
    debt_amount = serializers.FloatField()
    interest = serializers.IntegerField()
    is_debt_closed = serializers.BooleanField()










