from django.contrib.auth import get_user_model
from django.test import TestCase
from tags.models import Tag, SharedTag
from guardian.shortcuts import assign_perm

User = get_user_model()


class TagTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='user',
            password='test',
        )
        self.user.save()

        self.tag = Tag.objects.create(user=self.user, uid='1')
        self.tag.save()

    def test_unauthorized(self):
        self.assertFalse(self.user.has_perm('change_tag', self.tag))
        assign_perm('list_tags', self.user, self.tag)
        self.assertTrue(self.user.has_perm('change_tag', self.tag))


class SharedTagTestCase(TestCase):
    def setUp(self):
        self.user_1, created = User.objects.get_or_create(
            username='user_1',
            password='test',
        )
        self.user_2, created = User.objects.get_or_create(
            username='user_2',
            password='test',
        )

        self.tag = Tag.objects.create(user=self.user_1, uid='1')
        self.tag.save()

        self.shared_tag, created = SharedTag.objects.get_or_create(
            tag=self.tag,
            user=self.user_2,
        )

    def test_priviledges(self):
        self.assertTrue(
            self.user_1.has_perm('tags.view_shared_tag', self.shared_tag),
        )
        self.assertTrue(
            self.user_1.has_perm('tags.change_shared_tag', self.shared_tag),
        )

        self.assertTrue(
            self.user_2.has_perm('tags.view_shared_tag', self.shared_tag),
        )
        self.assertFalse(
            self.user_2.has_perm('tags.change_shared_tag', self.shared_tag),
        )
