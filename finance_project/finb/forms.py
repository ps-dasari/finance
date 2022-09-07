from calendar import c
from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import  *
from django.core.exceptions import ValidationError
import re



class company_mforms(forms.ModelForm):
    class Meta:
        #password=forms.CharField(widget=forms.PasswordInput)
        model = company_models
        fields =['name','logo','email','password','re_enter_password', 'mobile_number','company_name','company_address','interest_rate_followed']
        Widgets={
            'password': forms.PasswordInput(),
            're_enter_password': forms.PasswordInput(render_value=True),
        }
    def clean_mobile_number(self):
        inputmobile_number = self.cleaned_data['mobile_number']
        m=re.fullmatch(r'[6-9][0-9]{9}$',  inputmobile_number)
        if m != None:
            return inputmobile_number
        else:
            raise ValidationError("invalid mobile number")
    def clean(self):
        total_cleaned_data = super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['re_enter_password']
        if pwd==rpwd:
            return total_cleaned_data
        else:
            raise ValidationError("Incorrect password matching")

class accounts_mforms(forms.ModelForm):
    class Meta:
        model = accounts_models
        fields ='__all__'
    def clean(self):
        total_cleaned_data = super().clean()
        dept_amount=total_cleaned_data['dept_amount']
        is_debt_closed=total_cleaned_data['is_debt_closed']
        if dept_amount!=0:
            return is_debt_closed==False 
        else:
            return is_debt_closed==True 
    
    def __init__(self, *args, **kwargs):
        super(accounts_mforms, self).__init__(*args, **kwargs)
        self.fields['areas_models'].queryset = areas_models.objects.filter(title__isnull=False)
            
class customer_mforms(forms.ModelForm):
    class Meta:
        model = customer_models
        fields ='__all__' #['name','mobile_number','photo','area_code','customer_address']
    def clean_mobile_number(self):
        inputmobile_number = self.cleaned_data['mobile_number']
        m=re.fullmatch(r'[6-9][0-9]{9}$',  inputmobile_number)
        if m!= None:
            return inputmobile_number
        else:
            raise ValidationError("invalid mobile number")


class areas_mforms(ModelForm):
    class Meta:
        model = areas_models
        fields ='__all__'
    def clean_area_code(self):
        inputarea_code = self.cleaned_data['area_code']
        if len(inputarea_code)>4:
            raise ValidationError("area code must in 4 characters or less")
        else:
            return inputarea_code








   

