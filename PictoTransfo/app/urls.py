from django.urls import path
from .views import uploadPhoto, convertBw, resize, fusion, gif

urlpatterns = [
    path('', uploadPhoto.upload_photo, name='upload_photo'),
    path('home/', uploadPhoto.upload_photo, name='upload_photo'),
    path('resize/', resize.resizeImage, name='resize'),
    path('fusion/', fusion.imageFusion, name='fusion'),
    path('convert-bw/', convertBw.renderBw, name='convert_to_bw'),
    path('create-gif/', gif.create_gif_view, name='create_gif')
]
