import random
from datetime import datetime, timedelta

from django.core.management import BaseCommand
from django_seed import Seed

from reservations.models import Reservation
from rooms.models import Room
from users.models import User


class Command(BaseCommand):
    help = "Seeds Reservation"

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, help="Create new  Reservation")

    def handle(self, *args, **options):
        number = options['number']
        users = User.objects.all()
        rooms = Room.objects.all()

        seed = Seed.seeder()

        seed.add_entity(Reservation, number, {
            "guest": lambda x: random.choice(users),
            "room": lambda x: random.choice(rooms),
            "check_in": lambda x: datetime.now(),
            "check_out": lambda x: datetime.now() + timedelta(days=random.randint(1, 365)),
        })

        seed.execute()
        self.stdout.write(self.style.SUCCESS(f"Successfully created {number} new Reservation"))
