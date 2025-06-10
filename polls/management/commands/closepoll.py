from django.core.management.base import BaseCommand, CommandError, CommandParser
from polls.models import Question


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.allow_abbrev = False
        parser.add_argument("--cleardb",action='store_true',default=False)

    def handle(self, *args, **options):
        print(options)
        if options["cleardb"]:
            Question.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("db is empty!"))

