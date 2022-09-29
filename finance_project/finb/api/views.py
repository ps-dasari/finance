from os import stat
from django.shortcuts import render
# from urllib import request
from finb.models import *
from finb.forms import *
from finb.api.serializers import *
from finb import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .permissions import IsAdminOrReadOnly

#Create your views here.


def company_view(request):
    form = company_mforms()
    if request.method == 'POST':
        form = company_mforms(request.POST or None)
        if form.is_valid():
            form.save()
            print('name', form.cleaned_data['name'])
            print('company_name', form.cleaned_data['company_name'])
    company = company_models.objects.all()
    return render(request, 'company.html', {'form': form, 'company': company})


@api_view(['GET', 'POST'])
@permission_classes([IsAdminOrReadOnly])
def company_List(request):
    serializer = company_serializer()
    if request.method == 'GET':
        try:
            List = company_models.objects.all()
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = company_serializer(List, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
       serializer = company_serializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           serializer_dict = serializer.data
           serializer_dict['message'] = 'company details created successfully'
           return Response(serializer_dict, status=status.HTTP_201_CREATED)
       else:
           return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminOrReadOnly])
def company_Details(request, pk):
    serializer = company_serializer()
    if request.method == 'GET':
        try:
            List = company_models.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = company_serializer(List)
        serializer_dict = serializer.data
        serializer_dict['messages'] = 'company details'
        return Response(serializer_dict, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = company_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict = serializer.data
            serializer_dict['messages'] ='company details updated successfully'
            return Response(serializer_dict, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        List = company_models.objects.get(pk=pk)
        try:
            List.delete()
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def customer_List(request):
    serializer=customer_serializer()
    if request.method == 'GET':
        try:
            List=customer_models.objects.all()
        except ObjectDoesNotExist:
            serializer_error=serializer.errors
            serializer_error['message']='No customer details found.'
            return Response(serializer_error, status=status.HTTP_400_BAD_REQUEST)
        serializer=customer_serializer(List,many=True)
        serializer_dict = serializer.data
        serializer_dict['messages']='customer details created successfully.'
        return Response(serializer_dict, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=customer_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict= serializer.data
            serializer_dict['messages']='customer details created successfully.'
            return Response(serializer_dict, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def customer_Detail(request,pk):
    serializers =customer_serializer()
    if request.method=='GET':
        try:
            List=customer_models.objects.get(pk=pk)
        except ObjectDoesNotExist:
            serializer_error=serializer.errors
            serializer_error['message']='customer details not found'
            return Response(serializer_error,status=status.HTTP_204_NO_CONTENT)
        serializer=customer_serializer(List)
        serializer_dict=serializer.data
        return Response(serializer_dict,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=customer_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict=serializer.data
            serializer_dict['message']='successfully saved customer details'
            return Response(serializer_dict,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        List=customer_models.objects.get(pk=pk)
        try:
            List.delete()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def areas_List(request):
    serializer=areas_serializer()
    if request.method=='GET':
        try:
            List=areas_models.objects.all()
        except ObjectDoesNotExist:
            serializer_error=serializer.errors
            serializer_error['message']='area details not found '
            return Response(serializer_error,status=status.HTTP_204_NO_CONTENT)
        serializer=areas_serializer(List,many=True)
        serializer_dict=serializer.data
        serializer_dict['message']='area details found'
        return Response(serializer_dict,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=areas_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict=serializer.data
            serializer_dict['message']='area details created successfully'
            return Response(serializer_dict,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def area_Details(request,pk):
    serializer=areas_serializer()
    if request.method=='GET':
        try:
            List=areas_models.objects.get(pk=pk)
        except ObjectDoesNotExist:
            serializer_error=serializer.errors
            serializer_error['message']='{} details not found'.format(List.area_name)
        serializer=areas_serializer(List,many=True)
        serializer_dict=serializer.data
        return Response(serializer_dict,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=areas_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict=serializer.data
            serializer_dict['message']='area details updated successfully'
            return Response(serializer_dict,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='delete':
        List=areas_models.objects.get(pk=pk)
        try:
            List.delete()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def accounts_List(request):
    if request.method=='GET':
        serializer=accounts_serializer()
        try:
            List=accounts_models.objects.all()
        except:
            serializer_error=serializer.errors
            serializer_error['message']='account details not found'
            return Response(serializer_error,status=status.HTTP_400_BAD_REQUEST)
        #serializer=accounts_serializer(List,many=True)
        serializer_dict=serializer.data
        serializer_dict['message']='account details found'
        return Response(serializer_dict,status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer=accounts_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict=serializer.data
            serializer_dict['message']='account details created successfully'
            return Response(serializer_dict,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def accounts_Detail(request,pk):
    serializer=accounts_serializer()
    if request.method=='GET':
        try:
            List=accounts_models.objects.all()
        except:
            serializer_error=serializer.errors
            serializer_error['message']='account details not found'
            return Response(serializer_error,status=status.HTTP_204_NO_CONTENT)
        serializer=accounts_serializer(List)
        serializer_dict=serializer.data
        serializer_dict['message']='account details found'
        return Response(serializer_dict,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=accounts_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict=serializer.data
            serializer_dict['message']='account details updated successfully'
            return Response(serializer_dict,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        List=accounts_models.objects.get(pk=pk)
        try:
            List.delete()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

#
#
# class accountsList(generics.ListCreateAPIView):
#     queryset = accounts_models.objects.all()
#     serializer_class = accounts_serializer
#
#
# class accountsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = accounts_models.objects.all()
#     serializer_class = accounts_serializer
