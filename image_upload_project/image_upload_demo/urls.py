from django.urls import path
from . import views

app_name = 'image_upload_demo'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
]
