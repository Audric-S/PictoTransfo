import os
from django.conf import settings
from django.shortcuts import render
from PIL import Image
from .shared import uploadPhoto


def convertToBw(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    return img.point(lambda p: p > 128 and 255)



def renderBw(request):
    if request.method == 'POST':

        uploadPhoto.upload_photo(request);

        image_path = 'media/photo.png'
       
        bw_img = convertToBw(image_path)

        bw_img.save('media/image_bw.png')

        pathUrlBw = '../media/image_bw.png'

        pathUrl = '../media/photo.png'

        return render(request, 'convert-bw.template.html', {
            'pathURL': pathUrl,
            'pathURLBw': pathUrlBw
        })
    return render(request, 'convert-bw.template.html')
