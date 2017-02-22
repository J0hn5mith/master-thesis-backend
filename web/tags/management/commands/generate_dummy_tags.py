import sys
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
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

        for i, user in enumerate(User.objects.all()):
            if len(user.tags.all()) < num_tags:
                for j in range(num_tags):
                    Tag.objects.get_or_create(
                        uid=str(user.id) + "_" + str(j),
                        name="Tag " + str(j),
                        short_name="t_" + str(j),
                        user=user,
                    )
