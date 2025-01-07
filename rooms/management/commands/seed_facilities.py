from django.core.management import BaseCommand
from rooms import models as rooms_models


class Command(BaseCommand):
    help = "Seed Facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument('--times', type=int)

    def handle(self, *args, **options):
        facilities = [
            "En-suite bathroom, completely private! 1 WC on the ground floor 🛌",
            "Large wardrobe that can fit all your luggage!",
            "Dressing table with chair.🪞",
            "Large window to welcome sunlight and city view 🪟",
            "Hairdryer and Iron",
            "Living room with long and soft sofa, enough for your family to gather, watch TV, We have Youtube Premium, NetFlix account available for you to use and gather together",
            "We have small games to help you entertain with friends and family such as Chess - Chinese Chess ♟️"
        ]

        for facility in facilities:
            rooms_models.Facility.objects.create(name=facility)

        self.stdout.write(self.style.SUCCESS("Successfully created Facilities"))
