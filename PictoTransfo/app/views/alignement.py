from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from PIL import Image


def alignementView(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        img1 = request.FILES.get('picture1')
        img2 = request.FILES.get('picture2')
        alignment = request.POST.get('alignment')
        img1 = Image.open(img1)
        img2 = Image.open(img2)
        if alignment == 'vertical':
            saved_file_name = alignVertical(img1,img2)
        elif alignment == 'horizontal':
            saved_file_name = alignHorizontal(img1,img2)

        # Construire l'URL complète pour le fichier enregistré
        pathUrl = fs.url(saved_file_name)

        return render(request, 'alignement.template.html', {
            'pathURL': pathUrl + "alignement.png"
        })

    return render(request, 'alignement.template.html')
def alignHorizontal(img1,img2):
    fs = FileSystemStorage()

    imgFinal1 = img1.resize((max(img1.size[0], img2.size[0]), max(img1.size[1], img2.size[1])),Image.Resampling.LANCZOS)
    imgFinal2 = img2.resize((imgFinal1.size[0], imgFinal1.size[1]), Image.Resampling.LANCZOS)

    verticalPicture = Image.new("RGBA", (imgFinal1.size[0]*2, imgFinal1.size[1]), (0, 0, 0, 0))
    verticalPicture.paste(imgFinal1)
    verticalPicture.paste(imgFinal2,(imgFinal1.size[0],0))


    # Vérifier si un fichier avec le même nom existe déjà
    if fs.exists('alignement.png'):
        # Si un fichier avec le même nom existe déjà, le supprimer
        fs.delete('alignement.png')

    return verticalPicture.save('media/alignement.png')

def alignVertical(img1,img2):
    fs = FileSystemStorage()

    imgFinal1 = img1.resize((max(img1.size[0],img2.size[0]),max(img1.size[1],img2.size[1])), Image.Resampling.LANCZOS)
    imgFinal2 = img2.resize((imgFinal1.size[0],imgFinal1.size[1]), Image.Resampling.LANCZOS)

    horizontalPicture = Image.new("RGBA",(imgFinal1.size[0],imgFinal1.size[1]*2),(0, 0, 0, 0))
    horizontalPicture.paste(imgFinal1)
    horizontalPicture.paste(imgFinal2,(0,imgFinal1.size[1]))

    # Vérifier si un fichier avec le même nom existe déjà
    if fs.exists('alignement.png'):
        # Si un fichier avec le même nom existe déjà, le supprimer
        fs.delete('alignement.png')

    return horizontalPicture.save('media/alignement.png')

def resizePicture(img, width, height):
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return img









    imageHorizontal = Image.new("RGBA",(finalWidth,finalHeight2),(0, 0, 0, 0))
    imageHorizontal.paste(imgFinal1)
    imageHorizontal.paste(imgFinal2,(0,finalHeight))

    imageHorizontal.save('media/alignement.png')
