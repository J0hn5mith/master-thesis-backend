import os
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def upload_file(request):
    data = request.FILES['image']
    path = default_storage.save(
        'tmp/{0}'.format(data.name), ContentFile(data.read())
    )
    tmp_file = os.path.join(settings.MEDIA_URL, path)
    return JsonResponse({'url': tmp_file})
