from django.shortcuts import render
from PIL import Image

def resizeImage(request):
    if request.method == 'POST':
        width = int(request.POST['width'])
        height = int(request.POST['height'])

        image_path = 'media/photo.jpg'
        image = Image.open(image_path)
        
        image = image.convert('RGB')

        resized_image = image.resize((width, height))

        resized_image_path = 'media/image_resize.jpg'

        resized_image.save(resized_image_path)

        return render(request, 'resize.template.html')
    else:
        return render(request, 'resize.template.html')
