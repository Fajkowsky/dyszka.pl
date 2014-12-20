from django.core.management.base import BaseCommand
from subprocess import call


class Command(BaseCommand):
    help = 'Make coverage report for tests.'

    def handle(self, *args, **options):
        call(["coverage", "run", "manage.py", "test"])
        call(["coverage", "html"])
        call(["chromium-browser", "htmlcov/index.html"])