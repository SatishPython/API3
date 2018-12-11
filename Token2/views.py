from django.shortcuts import render
from .models import Products
from .serializers import ProductSeralizer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly

def input(request):
    return render(request,'input.html')
def insert(request):
    pid1 = int(request.GET['t1'])
    pname1 = request.GET['t2']
    pcost1 = float(request.GET['t3'])
    pmfdt1 = request.GET['t4']
    pexpdt1 = request.GET['t5']
    f = Products(pid=pid1,pname=pname1,pcost=pcost1,pmfdt=pmfdt1,pexpdt=pexpdt1)
    f.save()
    return request(request,'links.html')
def display(request):
    rec = Products.objects.all()
    return render(request,'display.html',{'records':rec})

class ProductList(generics.ListCreateAPIView):
    Queryset =Products.objects.all()
    Serializer_class = ProductSeralizer
    premission_class = (IsAdminOrReadOnly)



