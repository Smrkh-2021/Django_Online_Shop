from django.core.management import BaseCommand, CommandError
from argparse import ArgumentParser
from core.models import User


class Command(BaseCommand):
    help = 'A django command for active or deactive user'

    def add_arguments(self, parser:ArgumentParser):
        parser.add_argument('-u', '--username', required=True)

    def handle(self, *args, **options):
        username = options['username']
        try:
            self.user = User.objects.get(username=username)
        except:
            raise CommandError('user not found')








