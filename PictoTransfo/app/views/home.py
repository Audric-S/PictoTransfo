from django.shortcuts import render
from PIL import Image
import numpy as np




def home(request):
    if request.method == 'GET':
        return render(request, 'home.template.html')
