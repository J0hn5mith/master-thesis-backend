from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from rest_framework.test import APIClient
from tags.models import Tag
from tags.views import TagViewSet
from rest_framework import status

User = get_user_model()


class TagRESTTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test',
            password='test',
        )
        self.user.save()
        self.client = APIClient()
        # Required because normal login doesn't work due to 2 phase auth
        self.tag = Tag.objects.create(user=self.user, uid='1')
        self.tag.save()
        self.url_list = reverse('tag-list')
        self.url_detail = reverse_lazy(
            'tag-detail', kwargs={'pk': self.tag.pk}
        )


    def test_extract_file_name(self):
        self.client.force_authenticate(self.user)
        string = 'https://{0}/{1}/image/name.jpg'.format(
            settings.PAGE_URL, settings.MEDIA_URL
        )
        match = TagViewSet._extract_file_name(string)
        self.assertEqual(match, '//image/name.jpg')

    def test_get(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data['name'] = 'new name'
        response = self.client.put(
            self.url_detail, response.data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_authentication(self):
        response = self.client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_missing_authorization(self):
        self.unauthorized_user, created = User.objects.get_or_create(
            username='unauthorized_user',
            password='test',
        )
        response = self.client.force_authenticate(self.unauthorized_user)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


        # self.admin_user, created = User.objects.get_or_create(
            # username='admin_uaser',
            # password='test',
        # )

        # Admin User

        # Authorized user

        # Unauthorized  user


class SharedTagRESTTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test',
            password='test',
        )
        self.user.save()

        self.tag = Tag.objects.create(user=self.user)
        self.tag.save()

        self.client = APIClient()
        # Required because normal login doesn't work due to 2 phase auth
        self.client.force_authenticate(self.user)

        self.url = reverse_lazy('sharedtag-list')

    def test_create(self):
        data = {
            'permissions': 0,
            'user_id': self.user.pk,
            'tag_id': self.tag.pk,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
