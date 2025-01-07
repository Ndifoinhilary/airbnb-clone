from django.db import models
from core import  models as core_models

# Create your models here.


class List(core_models.TimeStampedModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="lists")
    rooms = models.ManyToManyField("rooms.Room", related_name="rooms", blank=True)

    def __str__(self):
        return self.name


    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of rooms"