import random

from django.contrib.admin.utils import flatten
from django.core.management import BaseCommand
from django_seed import Seed

from lists.models import List
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

        seed = Seed.seeder()

        seed.add_entity(List, number, {
            "user": lambda x: random.choice(users),
        })

        created_list =  seed.execute()
        cleaned_list = flatten(list(created_list.values()))
        for pk in cleaned_list:
            list_created = List.objects.get(pk=pk)
            for i in range(3, random.randint(1, 10)):
                list_created.rooms.add(i)

        self.stdout.write(self.style.SUCCESS(f"Successfully created {number} new reviews"))
