import time

from django.core.management.commands.migrate import Command

from django.db import connections
from django.db.utils import OperationalError


class Command(Command):
    """
    Wait for the default database to be ready before running migrations
    """

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        connected, start = False, time.time()
        maximum_wait = 15
        while not connected and time.time() - start < maximum_wait:
            try:
                connections['default'].cursor().execute("SELECT 1")
                connected = True
            except OperationalError:
                self.stdout.write("waiting for database...")
                time.sleep(maximum_wait // 3)
        if time.time() - start > maximum_wait:
            raise OperationalError("Could not connect to database.")

        self.stdout.write(self.style.SUCCESS('Database available!'))

        super().handle(*args, **options)
