import random

from django.contrib.admin.utils import flatten
from django.core.management import BaseCommand
from django_seed import Seed

from rooms import models as rooms_models
from users.models import User


class Command(BaseCommand):
    help = "To seed rooms or create new rooms"

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, help="Create new rooms")


    def handle(self, *args, **options):
        users = User.objects.all()[:25]
        room_type = rooms_models.RoomType.objects.all()
        number = options["number"]
        seeder = Seed.seeder()
        seeder.add_entity(rooms_models.Room, number, {
            "name":lambda x: seeder.faker.name(),
            "guest":lambda x: random.randint(1, 10),
            "beds":lambda x: random.randint(1, 10),
            "bedrooms":lambda x: random.randint(1, 10),
            "baths":lambda x: random.randint(1, 10),
            "host": lambda x : random.choice(users),
            "room_type": lambda x : random.choice(room_type),
        })
        house_rule = rooms_models.HouseRule.objects.all()
        amenities = rooms_models.Amenity.objects.all()
        facilities = rooms_models.Facility.objects.all()
        seed_rooms =  seeder.execute()
        clean_room =  flatten(list(seed_rooms.values()))
        for pk in clean_room:
            room = rooms_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                rooms_models.Photo.objects.create(
                    caption = seeder.faker.sentence() ,
                    room=room,
                    file = f"room_photos/{random.randint(1,31)}.webp"

                )
            for a in amenities:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, 10)
                if magic_number % 2 != 0:
                    room.facilities.add(f)

            for h in house_rule:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    room.house_rules.add(h)

        self.stdout.write(self.style.SUCCESS(f"{number} of rooms created"))
