from django.shortcuts import render
from PIL import Image
from .shared import uploadPhoto

def resizeImage(request):
    if request.method == 'POST':
        width = int(request.POST['width'])
        height = int(request.POST['height'])

        uploadPhoto.upload_photo(request)

        image_path = 'media/photo.png'
        image = Image.open(image_path)
        
        image = image.convert('RGB')

        resized_image = image.resize((width, height))

        resized_image_path = 'media/image_resize.png'

        resized_image.save(resized_image_path)

        resized_image_path = '../media/image_resize.png'

        return render(request, 'resize.template.html', {
            'pathURL': image_path,
            'pathURLResize': resized_image_path
        })
    
    return render(request, 'resize.template.html')
