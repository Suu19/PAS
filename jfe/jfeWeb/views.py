
from itertools import count
from django.shortcuts import render
from django.db.models import Count
from jfeWeb.models import JfeData


# Create your views here.

def homeView(request):   
    data=JfeData.objects.values('last_update').annotate(count=Count('last_update'))
    return render(request,'home.html',{'data':data})

def listView(request,id):
    data=JfeData.objects.filter(last_update=id)
    return render(request,'list.html',{'data':data})

def detailView(request,id):
    data=JfeData.objects.get(id=id)       
    return render(request,'detail.html',{'data':data})