from django.test import TestCase
from rest_framework.test import force_authenticate, APIRequestFactory
from tags.models import Tag
from alarm.models import AlarmConfig
from alarm.serializers import AlarmConfigSerializer

factory = APIRequestFactory()
request = factory.get('/accounts/django-superstars/')

class AlarmConfigSerializeTrestCase(TestCase):

    def setUp(self):
        tag = Tag.objects.create() # Creates alarm config by signal
        tag.save()

    def test_instanciation(self):
        """Animals that can speak are correctly identified"""
        try:
            alarm_config = AlarmConfig.objects.all().first()
            s = AlarmConfigSerializer(alarm_config, context={'request': request})
            s.data
            self.assertTrue(True)
        except:
            self.assertTrue(False)
