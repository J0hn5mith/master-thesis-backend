from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()
client = APIClient()


class UserRESTTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test', password='test', email='test@test.com'
        )
        self.url_list = reverse('user-list')
        self.url_detail = reverse_lazy(
            'user-detail', kwargs={'pk': self.user.pk}
        )

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data['email'] = 'new.mail@example.ch'
        response = client.put(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CurrentUserRESTTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test', password='test', email='test@test.com'
        )
        self.url = reverse('user-current')

    def test_get(self):
        response = client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        client.force_authenticate(self.user)
        response = client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserConfigurationRESTTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test', password='test', email='test@test.com'
        )
        self.url_list = reverse('userconfiguration-list')
        self.url_detail = reverse_lazy(
            'userconfiguration-detail', kwargs={'pk': self.user.conf.pk}
        )

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data['notify_by_mail'] = 'true'
        response = client.put(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
