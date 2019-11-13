from django.shortcuts import render
from rendering.models import Rendering
from .forms import AddForm
from . import models
import cv2
import urllib
import numpy
import os
import io
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your views here.
def uploadImg(request):
    # 判断是否为 post 方法提交 
    if request.method == "POST":
        #image= request.FILES.get("img")
        stream=request.FILES.get("img")
        im = Image.open(stream) 
        img = cv2.cvtColor(numpy.asarray(im),cv2.COLOR_RGB2BGR)   
        dst=rendering(img)
        image = Image.fromarray(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
        img_io = io.BytesIO()
        image.save(img_io,format='JPEG') 
       
        img2 = InMemoryUploadedFile(img_io,None,'123.jpg','image/jpeg',img_io.seek(0,os.SEEK_END),None)
        new_img=Rendering(
             document=img2
            )
       # src =cv2.imread(new_img,cv2.IMREAD_COLOR
        new_img.save ()
    #img2=cv2.imread("./media/img/eminem.jpg")
    
   
   
    
    return render(request,'rendering/uploading.html')

def rendering(image):
    dst = cv2.edgePreservingFilter(image, flags=1, sigma_s=100, sigma_r=1.3)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 10))
    dst2 = cv2.erode(dst,kernel)
     
    return dst2




def showImg(request):
   
   
    
   img = models.Rendering.objects.all()
   content={
        'img':img,
        }     
   return render(request,'rendering/showing.html',content)
# Create your views here.


