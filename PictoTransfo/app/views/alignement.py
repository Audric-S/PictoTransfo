from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import imageio
from PIL import Image


def alignementView(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        forms = request.FILES.getlist('pictures')
        pictures = []
        for picture in forms:
            img = Image.open(picture)
            pictures.append(img)

        duration = int(request.POST.get('duration')) * 1000
        saved_file_name = makeGif(pictures, duration)
        pathURL = fs.url(saved_file_name)
        return render(request, 'gif.template.html', {'pathURL': pathURL})
    return render(request, 'alignement.template.html')


def makeGif(pictures, duration):
    # We create an empty array to store the pictures.
    gif = []
    for picture in pictures:  # We loop through the pictures
        redPicture = picture.convert("RGB")
        # If the picture is not the same size as the first one, resize it
        if pictures[0].size != picture.size:
            redPicture = redPicture.resize(pictures[0].size)
        # append the image to the gif array
        gif.append(redPicture)
    # To convert the duration of form per image
    duration = duration / len(pictures)
    # Register the GIF in the media folder
    return imageio.mimsave('media/pictoTransfoGif.gif', gif, duration=duration, loop=0)
