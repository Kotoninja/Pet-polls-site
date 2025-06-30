from django.core.management.base import BaseCommand
from polls.models import Question


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.allow_abbrev = False
        parser.add_argument("--cleardb", action="store_true", default=False,help='cleans Question db')

    def handle(self, *args, **options):
        """
        WARNING: If we write --cleardb, all Question database is cleans
        """
        print(options)
        if options["cleardb"]:
            Question.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("db is empty!"))
