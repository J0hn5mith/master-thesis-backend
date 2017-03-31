from django.http import JsonResponse
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

    def update(self, request, pk, format=None):
        """
        Custom implementation to deal with image.
        """
        tag = self.get_object()
        print(tag.avatar)
        serializer = TagSerializer(
            tag,
            data=request.data,
            context={'request': request},
        )
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


def tag_prototype_view(request):
    new_tag = Tag(user=request.user)
    serializer = TagSerializer(
        new_tag,
        context={'request': request},
    )
    return JsonResponse(serializer.data)
