import os
from django.conf import settings
from django.shortcuts import render
from PIL import Image

def convert_to_bw(image_path):
    img = Image.open(image_path)
    bw_img = img.convert("1")
    return bw_img

    #FAIRE VERIF SI IMG EXIST SINON RAISE EXCEPTION

def hello_world(request):
    if request.method == 'GET':
        image_path = 'media/photo.jpg'
       
        bw_img = convert_to_bw(image_path)

        bw_img.save('media/image_bw.jpg')

        return render(request, 'convert-bw.template.html')