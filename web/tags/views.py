from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from tags.serializers import TagSerializer
from tags.models import Tag

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return self.request.user.tags.all().order_by('pk')
