from django.core.management import BaseCommand
from django_seed import Seed

from rooms import models as rooms_models


class Command(BaseCommand):
    help = "Seed House Rules"

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, help='Number of houses')

    def handle(self, *args, **options):
        seed = Seed.seeder()
        number = options['number']
        seed.add_entity(rooms_models.HouseRule, number, {
            "name": seed.faker.sentence(),
        })

        seed.execute()

        self.stdout.write(self.style.SUCCESS(f"Successfully {number} houses rules"))

