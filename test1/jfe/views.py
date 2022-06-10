from django.shortcuts import render
from django.views.generic import TemplateView
import os
from glob import glob
from PIL import Image
import glob
from requests import Request
from .models import *
from django.contrib.auth.models import *


# Create your views here.
#class HomePageView(TemplateView):
 #   template_name= "index.html"

def aboutPageView(request):
    return render(request,'hello.html')

    
def getImageName(folder):
    img_list=[]
    for image in glob.glob(folder):
        if image is not None:
            imageName=Image.open(image)
            imagefile=imageName.filename
            img=os.path.basename(imagefile)
            img_list.append(img)
    return img_list

def HomePageView(request,id):
      images=Pushtodatabase.objects.get(image_id=id)
      return render(request,'index.html',{'images':images})

def listPageView(request):
    images=Pushtodatabase.objects.all()
    return render(request,'about.html',{'images':images})
