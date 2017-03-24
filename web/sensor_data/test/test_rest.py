from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from rest_framework.test import APIClient
from django.contrib.gis.geos import Point
from sensor_data.models import PositionMeasurement
from rest_framework import status

client = APIClient()


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

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.delete(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SensorDataPost(TestCase):
    def setUp(self):
        self.url = reverse('post-sensor-data')

    def test_post(self):
        response = client.put(
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
