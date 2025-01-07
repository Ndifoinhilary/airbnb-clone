from django.core.management import BaseCommand
from rooms import models as rooms_models


class Command(BaseCommand):
    help = "Seed amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument('--times', type=int)

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Wifi",
            "Dedicated workspace",
            "Free parking on premises",
            "TV",
            "Washer",
            "Dryer",
            "Exterior security cameras on property",
            "Hair dryer",
            "Cleaning products",
            "Shampoo",
            "Body soap",
            "Hot water",
            "Shower gel",
        ]

        for amenity in amenities:
            rooms_models.Amenity.objects.create(name=amenity)

        self.stdout.write(self.style.SUCCESS("Successfully created Amenities"))

