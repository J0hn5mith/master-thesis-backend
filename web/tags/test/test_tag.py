from django.contrib.auth import get_user_model
from django.test import TestCase
from tags.models import Tag
from guardian.shortcuts import assign_perm

User = get_user_model()


class TagTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test',
            password='test',
        )
        self.user.save()

        self.tag = Tag.objects.create(user=self.user, uid='1')
        self.tag.save()

    def test_unauthorized(self):
        self.assertFalse(self.user.has_perm('change_tag', self.tag))
        assign_perm('list_tags', self.user, self.tag)
        self.assertTrue(self.user.has_perm('change_tag', self.tag))
