from os import stat
from django.shortcuts import render
from finb.models import *
from finb.forms import *
from finb.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

#Create your views here.
def company_view(request):
    form=company_mforms()
    if request.method=='POST':
        form=company_mforms(request.POST)
        form.is_valid()
        form.save()
        print('name',form.cleaned_data['name'])
        print('company_name',form.cleaned_data['company_name'])
    company=company_models.objects.all()
    return render(request,'company.html', {'form':form,'company':company})

@api_view(['GET', 'POST'])
def company_api(request):
    if request.method=='GET':
        company=company_models.objects.all()
        serializer= company_serializer(company,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer= company_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.validated_data
            print('name',serializer.data['name'])
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def company_api_i(request, pk):
    if request.method=='GET':
        try:
            company=company_models.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return  Response('no data in company with id:{}'.format(pk),status=status.HTTP_400_BAD_REQUEST)
        serializer=company_serializer(company)
        return Response(serializer.data)
    if request.method=='PUT':
        #company=company_models.objects.get(pk=pk)
        serializer=company_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        company=company_models.objects.get(pk=pk)
        company.delete()
        return Response('data is deleted',status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def customer_api(request):
    if request.method=='GET':
        try:
            customer=customer_models.objects.all()
        except ObjectDoesNotExist:
            return  Response('no data in customer',status=status.HTTP_400_BAD_REQUEST) 
        serializers=customer_serializer(customer,many=True)
        return Response(serializers.data)
    if request.method=='POST':
        serializers=customer_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()  
            print('name:',serializers.data['name'])
            print('area_code:',serializers.data['area_code'])
            return Response(serializers.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



