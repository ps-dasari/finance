from turtle import title
from django.contrib import admin
from finb.models import company_models,accounts_models,areas_models,customer_models
# Register your models here.

class company_admin(admin.ModelAdmin):
    list_display = ['id', 'name','logo','email','password','re_enter_password','mobile_number','company_name','company_address','interest_rate_followed']
admin.site.register(company_models,company_admin)

class customer_admin(admin.ModelAdmin):
    list_display = ['id','name','date','photo','area_code','customer_address']
admin.site.register(customer_models,customer_admin)

class areas_admin(admin.ModelAdmin):
    list_display = ['id','area_code','area_name']
admin.site.register(areas_models,areas_admin)

class accounts_admin(admin.ModelAdmin):
    list_display = [ 'name','mobile_number','lone_amount','area_code','lone_issue_date','daily_debt','number_of_days','paid_amount','debt_amount','interest','is_debt_closed']
    # def area_code(self,instance):
    #     return instance.areas_admin.area_code   
admin.site.register(accounts_models,accounts_admin)


