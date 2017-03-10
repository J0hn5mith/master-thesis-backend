from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from tags.serializers import TagSerializer
from tags.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        print(self.request.user)
        if hasattr(self.request.user, 'tags'):
            return self.request.user.tags.all().order_by('pk')
        return []

    def update(self, request, pk, format=None):
        """
        Custom implementation to deal with image.
        """
        tag = self.get_object()
        serializer = TagSerializer(tag, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            print(e);
            print(serializer.errors);
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
