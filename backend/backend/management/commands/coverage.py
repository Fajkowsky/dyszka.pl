from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Make coverage report for tests.'

    def handle(self, *args, **options):
        pass