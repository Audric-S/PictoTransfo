import os
from django.conf import settings
from django.shortcuts import render
from PIL import Image
from .shared import uploadPhoto

def convertToBw(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    return img



def renderGreyShades(request):
    if request.method == 'POST':
        uploadPhoto.upload_photo(request);

        image_path = 'media/photo.png'
       
        bw_img = convertToBw(image_path)

        bw_img.save('media/image_gs.png')

        pathURLgs = '../media/image_gs.png'

        pathUrl = '../media/photo.png'

        return render(request, 'grey-shades.template.html', {
            'pathURL': pathUrl,
            'pathURLgs': pathURLgs
        })
    return render(request, 'grey-shades.template.html')
