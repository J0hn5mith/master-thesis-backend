from django.test import TestCase
from django.urls import reverse, reverse_lazy
from rest_framework.test import APIRequestFactory, APIClient
from tags.models import Tag

factory = APIRequestFactory()
client = APIClient()


class AlarmConfigSerializeTrestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create()  # Creates alarm config by signal
        self.tag.save()
        self.url_list = reverse('alarmconfig-list')
        self.url_detail = reverse_lazy(
            'alarmconfig-detail', kwargs={'pk': self.tag.pk}
        )

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, 200)
        response.data['time_to_deactivate'] = 30
        response = client.put(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, 200)
