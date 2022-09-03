from django.shortcuts import render
from finb.models import *
from finb.forms import *
from finb.api.serializers import *
# Create your views here.
def company_view(request):
    form=company_forms()
    if request.method=='POST':
        form=company_forms(request.POST)
        form.is_valid()
        form.save()
        print('name',form.cleaned_data['name'])
        print('company_name',form.cleaned_data['company_name'])
    company=company_models.objects.all()
    return render(request,'company.html', {'form':form,'company':company})


