from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from rest_framework.test import APIClient
from tags.models import Tag
from tags.views import TagViewSet
from rest_framework import status

User = get_user_model()


class TagRESTTrestCase(TestCase):
    def setUp(self):
        self.test_user, created = User.objects.get_or_create(
            username='test',
            password='test',
        )
        self.test_user.save()
        self.client = APIClient()
        # Required because normal login doesn't work due to 2 phase auth
        self.client.force_authenticate(self.test_user)
        self.tag = Tag.objects.create(user=self.test_user)
        self.tag.save()
        self.url_list = reverse('tag-list')
        self.url_detail = reverse_lazy(
            'tag-detail', kwargs={'pk': self.tag.pk}
        )

    def test_extract_file_name(self):
        string = 'https://{0}/{1}/image/name.jpg'.format(
            settings.PAGE_URL, settings.MEDIA_URL
        )
        match = TagViewSet._extract_file_name(string)
        self.assertEqual(match, '/image/name.jpg')

    def test_get(self):
        response = self.client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        response = self.client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data['name'] = 'new name'
        response = self.client.put(
            self.url_detail, response.data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
