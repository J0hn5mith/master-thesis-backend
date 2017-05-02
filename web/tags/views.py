import re
from django.conf import settings
from django.core.files.base import ContentFile
from rest_framework import viewsets, status, generics, filters
import django_filters.rest_framework
from rest_framework.response import Response
from tags.serializers import TagSerializer, SharedTagSerializer
from tags.models import Tag, SharedTag
from .permissions import ExtendedObjectPermissions


class TagViewSet(viewsets.ModelViewSet):
    """
    A REST interface for accessing the Tag model.
    Required Authorization:
    * Owner of the tag
    * Admin
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (filters.DjangoObjectPermissionsFilter, )
    permission_classes = (ExtendedObjectPermissions, )

    def initialize_request(self, request, *args, **kwargs):
        request = super(TagViewSet, self).initialize_request(
            request, *args, **kwargs
        )
        file = request.data.get('avatar')
        if file:
            file_name = self._extract_file_name(file)
            file_name = '{0}{1}'.format(settings.MEDIA_ROOT, file_name)
            file = open(file_name, 'rb')
            self.avatar_file = ContentFile(file.read())
            request.data['avatar'] = None
        return request

    def perform_create(self, serializer):
        res = serializer.save()
        if hasattr(self, 'avatar_file'):
            res.avatar.save("test.jpg", self.avatar_file)

    def update(self, request, pk, format=None):
        """
        Custom implementation to deal with image.
        """

        tag = self.get_object()
        serializer = TagSerializer(
            tag,
            data=request.data,
            context={'request': request},
        )
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(avatar=tag.avatar)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def _extract_file_name(string):
        """
        Extracts the file name from image url.
        """
        if not string:
            return ''
        matches = re.search(
            r'(?<={0}).*(?=$)'.format(settings.MEDIA_URL), string
        )
        if (matches):
            return '/{0}'.format(matches[0])
        else:
            return ''


class SharedTagListView(generics.ListAPIView):
    queryset = SharedTag.objects.all()
    serializer_class = SharedTagSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filter_fields = ('permissions', 'tag__id')


class SharedTagViewSet(viewsets.ModelViewSet):
    queryset = SharedTag.objects.all()
    serializer_class = SharedTagSerializer
    filter_backends = (filters.DjangoObjectPermissionsFilter, )
    permission_classes = (ExtendedObjectPermissions, )

    def create(self, request):
        user_id = request.data['user_id']
        tag_id = request.data['tag_id']
        shared_tag = SharedTag.objects.create(
            permissions=0, user_id=user_id, tag_id=tag_id
        )
        serializer = self.get_serializer(shared_tag)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
