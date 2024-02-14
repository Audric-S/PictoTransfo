"""
URL configuration for PictoTransfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import uploadPhoto, convertBw, gif, resize, fusion

urlpatterns = [
    path('', uploadPhoto.upload_photo, name='upload_photo'),
    path('home/', uploadPhoto.upload_photo, name='upload_photo'),
    path('convert-bw/', convertBw.renderBw, name='convert_to_bw'),
    path('create-gif/', gif.create_gif_view, name='create_gif')
    path('convert-bw/', convertBw.hello_world, name='convert_to_bw'),
    path('resize/', resize.resizeImage, name='resize'),
    path('fusion/', fusion.imageFusion, name='fusion')

]
