import re
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def clean_filename(filename):
    # Remplacer les caractères spéciaux et les espaces par des tirets
    cleaned_filename = re.sub(r'[^\w\s.-]', '', filename)
    # Supprimer les espaces au début et à la fin du nom de fichier
    cleaned_filename = cleaned_filename.strip()
    return cleaned_filename


def getExtension(filename):
    # Récupérer l'extension du fichier
    extension = filename.split('.')[-1]
    return extension


def upload_photo(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        photo = request.FILES['photo']
        fs = FileSystemStorage()

        # Nettoyer le nom du fichier
        cleaned_filename = 'photo.png'

        # Vérifier si un fichier avec le même nom existe déjà
        if fs.exists(cleaned_filename):
            # Si un fichier avec le même nom existe déjà, le supprimer
            fs.delete(cleaned_filename)

        # Enregistrer le nouveau fichier
        saved_file_name = fs.save(cleaned_filename, photo)

        # Construire l'URL complète pour le fichier enregistré
        pathUrl = fs.url(saved_file_name)

        return render(request, 'upload.template.html', {
            'pathURL': pathUrl
        })

    return render(request, 'upload.template.html')
