import re
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def clean_filename(filename):
    cleaned_filename = re.sub(r'[^\w\s.-]', '', filename)
    cleaned_filename = cleaned_filename.strip()
    return cleaned_filename


def getExtension(filename):
    extension = filename.split('.')[-1]
    return extension


def upload_photo(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        photo = request.FILES['photo']
        fs = FileSystemStorage()

        cleaned_filename = 'photo.png'

        if fs.exists(cleaned_filename):
            fs.delete(cleaned_filename)

        saved_file_name = fs.save(cleaned_filename, photo)

    