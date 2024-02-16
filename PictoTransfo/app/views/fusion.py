from django.shortcuts import render
from PIL import Image
import numpy as np




def imageFusion(request):
    if request.method == 'POST' and request.FILES.get('back_image') and request.FILES.get('front_image'):
        img1 = Image.open(request.FILES['back_image'])
        img2 = Image.open(request.FILES['front_image'])
        
        blend_ratio = float(request.POST.get('blend_ratio', 0.5))
        position_x = int(request.POST.get('position_x', 0))
        position_y = int(request.POST.get('position_y', 0))
        
        if (np.asarray(img1).shape[-1] or  np.asarray(img2).shape[-1] == 4):
            if (np.asarray(img1).shape[-1] == 4):
                img1 = img1.convert("RGB")
            else:
                img2 = img2.convert("RGB")

        x, y = position_x, position_y
        x *= -1
        y *= -1
        
        img2 = img2.crop((x, y, x + img1.width, y + img1.height))

        arrayImg1 = np.array(img1)
        arrayImg2 = np.array(img2)

        blended_array = np.round(arrayImg1 * blend_ratio + arrayImg2 * (1 - blend_ratio)).astype(np.uint8)

        if blended_array.ndim == 2:
            blended_array = np.expand_dims(blended_array, axis=2)

        blended_img = Image.fromarray(blended_array, 'RGB')

        blended_img.save('media/fusion.png')

        pathURLfusion = '../media/fusion.png'

        return render(request, 'fusion.template.html', {
            'pathURLfusion': pathURLfusion
        })
    return render(request, 'fusion.template.html')
