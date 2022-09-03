from calendar import c
from django.forms import ModelForm
from django import forms
from .models import  company_models,accounts_models,areas_models,customer_models


class company_mforms(forms.ModelForm):
    class Meta:
        model = company_models
        fields ='__all__'
class accounts_mforms(forms.ModelForm):
    class Meta:
        model = accounts_models
        fields ='__all__'
class customer_mforms(forms.ModelForm):
    class Meta:
        model = customer_models
        fields ='__all__'
class areas_mforms(ModelForm):
    class Meta:
        model = areas_models
        fields ='__all__'

# class company_forms(forms.Form):
#     id=forms.IntegerField()
#     name=forms.CharField()
#     logo = forms.ImageField()
#     email=forms.EmailField()
#     password=forms.CharField()
#     re_enter_password=forms.CharField()
#     mobile_number=PhoneNumberField()
#     company_name=forms.CharField()
#     company_address=forms.CharField()
#     interest_rate_followed=forms.IntegerField()







   

