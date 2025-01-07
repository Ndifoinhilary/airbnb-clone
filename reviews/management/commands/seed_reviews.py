import random

from django.core.management import BaseCommand
from django_seed import Seed

from reviews.models import Review
from rooms.models import Room
from users.models import User


class Command(BaseCommand):
    help = "Seeds reviews"

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, help="Create new  reviews")

    def handle(self, *args, **options):
        number = options['number']
        users = User.objects.all()
        rooms = Room.objects.all()

        seed = Seed.seeder()

        seed.add_entity(Review, number, {
            "cleanliness": lambda x: random.randint(0, 5),
            "accuracy": lambda x: random.randint(0, 5),
            "check_in": lambda x: random.randint(0, 5),
            "communication": lambda x: random.randint(0, 5),
            "location": lambda x: random.randint(0, 5),
            "value": lambda x: random.randint(0, 5),
            "user": lambda x: random.choice(users),
            "room": lambda x: random.choice(rooms),
        })

        seed.execute()
        self.stdout.write(self.style.SUCCESS(f"Successfully created {number} new reviews"))
