from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
import imageio
from PIL import Image


def create_gif_view(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        forms = request.FILES.getlist('pictures')
        pictures = []
        for picture in forms:
            img = Image.open(picture)
            pictures.append(img)

        duration = int(request.POST.get('duration')) * 1000
        makeGif(pictures, duration)
        pathURL = FileSystemStorage('media/pictoTransfoGif.gif')
        return render(request, 'gif.template.html', {'pathURL': pathURL})
    return render(request, 'gif.template.html')


def makeGif(pictures, duration):
    gif = []  # We create an empty array to store the pictures.
    # Finally, we will save this array as a gif in media folder
    for picture in pictures:  # We loop through the pictures
        redPicture = picture.convert("RGB")
        # If the picture is not the same size as the first one, resize it
        if pictures[0].size != picture.size:
            redPicture = redPicture.resize(pictures[0].size)

        gif.append(redPicture)  # append the image to the gif array
    print(gif)
    # Register the GIF in the media folder
    imageio.mimsave('media/pictoTransfoGif.gif', gif, duration=duration, loop=0)
