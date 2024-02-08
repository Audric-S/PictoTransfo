from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def upload_photo(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        # Sauvegarder le fichier dans un dossier spécifique (par exemple 'photos')
        fs.save(photo.name, photo)
        pathUrl = '../media/' + photo.name
        return render(request, 'upload.template.html', {
            'pathURL': pathUrl
        })
    return render(request, 'upload.template.html')
