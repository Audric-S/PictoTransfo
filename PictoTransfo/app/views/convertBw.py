import os
from django.conf import settings
from django.shortcuts import render
from PIL import Image

def convert_to_bw(image_path):
    absolute_image_path = os.path.join(settings.BASE_DIR, 'app/assets', 'pictures', image_path)
    img = Image.open(absolute_image_path)
    bw_img = img.convert("1")
    return bw_img

def hello_world(request):
    if request.method == 'GET':
        image_path = 'image.jpg'

        original_image_path = os.path.join(settings.BASE_DIR, 'app/assets', 'pictures', image_path)

        bw_img = convert_to_bw(image_path)

        bw_image_path = os.path.join(settings.BASE_DIR, 'app/assets', 'pictures', 'bw_image.jpg')

        bw_img.save(bw_image_path)

        return render(request, 'convert-bw.template.html', {'original_image_path': original_image_path, 'bw_image_path': bw_image_path})
