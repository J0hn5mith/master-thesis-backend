import sys
import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from tags.models import Tag

User = get_user_model()


class Command(BaseCommand):
    help = 'Generates dummy tags for every user. '

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            dest='num_tags',
            default=10,
            type=int,
        )

    def handle(self, *args, **options):
        num_tags = int(options['num_tags'])
        self.delete_tags()
        self.create_tags(num_tags)


    def create_tags(self, num_tags):
        for i, user in enumerate(User.objects.all()):
            if len(user.tags.all()) < num_tags:
                for j in range(num_tags):
                    tag = Tag.objects.get_or_create(
                        uid=str(user.id) + "_" + str(j),
                        name="Tag " + str(j),
                        short_name="t_" + str(j),
                        user=user,
                        charge_status=random.random()*100,
                        last_update=timezone.now(),
                    )

    def delete_tags(self):
        for user in User.objects.all():
            for tag in user.tags.all():
                tag.delete()

