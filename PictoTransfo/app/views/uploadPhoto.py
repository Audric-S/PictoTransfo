from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def upload_photo(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        # Sauvegarder le fichier dans un dossier spécifique (par exemple 'photos')
        filename = fs.save('./app/assets/pictures/' + photo.name, photo)
        # Récupérer l'URL du fichier téléchargé
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.template.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.template.html')
