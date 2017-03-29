from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'file-upload', views.upload_file, name='file_upload'),
]
