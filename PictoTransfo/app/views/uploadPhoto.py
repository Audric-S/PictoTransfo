from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def upload_photo(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        # Sauvegarder le fichier dans un dossier spécifique (par exemple 'photos')
        fs.save('photo.jpg', photo)
    return render(request, 'upload.template.html')
