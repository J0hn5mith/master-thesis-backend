from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from rest_framework.test import APIClient
from django.contrib.gis.geos import Point
from sensor_data.models import PositionMeasurement
from rest_framework import status

User = get_user_model()


class SensorDataRESTTrestCase(TestCase):
    def setUp(self):
        self.sensor_data = PositionMeasurement.objects.create(
            uid='uid',
            time_stamp=timezone.now(),
            position=Point(0, 0),
        )
        self.url_list = reverse('positionmeasurement-list')
        self.url_detail = reverse_lazy(
            'positionmeasurement-detail', kwargs={'pk': self.sensor_data.pk}
        )
        self.user, created = User.objects.get_or_create(
            username='user',
            password='test',
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_get(self):
        response = self.client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_for_invalid_tag(self):
        pass

    def test_get_unauthorized(self):
        pass

    def test_delete(self):
        response = self.client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(
            self.url_detail, response.data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SensorDataPost(TestCase):
    def setUp(self):
        self.url = reverse('post-sensor-data')
        self.client = APIClient()

    def test_post(self):
        response = self.client.put(
            self.url,
            format='json',
            data={
                "sensor_id":
                "uid_1",
                "measurements": [
                    {
                        "time_stamp": "2017-03-23T14:38:18.968986418Z",
                        "position": {
                            "latitude": 47.4156,
                            "longitude": 8.512299
                        }
                    }, {
                        "time_stamp": "2017-03-23T14:39:18.968986418Z",
                        "position": {
                            "latitude": 47.5156,
                            "longitude": 8.612299
                        }
                    }
                ]
            }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "The response has wrong status code.",
        )
        self.assertEqual(
            len(PositionMeasurement.objects.all()),
            2,
            "Not enoguh measurements were created",
        )
        print(PositionMeasurement.objects.all().first().time_stamp)
