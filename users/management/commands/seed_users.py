from django.core.management import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "Create new users that are not supper users nor staffs"

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, help='Number of users to create')

    def handle(self, *args, **options):
        number = options['number']
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            "is_staff": False,
            "is_superuser": False,
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"Successfully created {number} users"))
