from typing import Any
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from users.models import UserInfo


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.allow_abbrev = False
        pass

    def handle(self, *args, **options) -> str | None:
        pass
