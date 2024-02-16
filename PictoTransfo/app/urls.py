from django.urls import path
from .views import convertBw, resize, fusion, gif, grey_shades, shared

urlpatterns = [
    path('', shared.uploadPhoto.upload_photo, name='upload_photo'),
    path('resize/', resize.resizeImage, name='resize'),
    path('fusion/', fusion.imageFusion, name='fusion'),
    path('convert-bw/', convertBw.renderBw, name='convert_to_bw'),
    path('create-gif/', gif.create_gif_view, name='create_gif'),
    path('grey-shades/', grey_shades.renderGreyShades, name='convert_to_gs')
]
