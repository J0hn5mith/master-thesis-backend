import re
from django.http import JsonResponse
from django.conf import settings
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from tags.serializers import TagSerializer
from tags.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'tags'):
            return self.request.user.tags.all().order_by('pk')
        return []

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


def tag_prototype_view(request):
    """
    Returns an empty tag datatype to fill in the front end.
    """
    new_tag = Tag(user=request.user)
    serializer = TagSerializer(
        new_tag,
        context={'request': request},
    )
    return JsonResponse(serializer.data)
