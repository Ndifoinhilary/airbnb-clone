from django.contrib.auth import get_user_model
from django.db import models


from core import  models as core_models
from rooms.models import Room

User = get_user_model()
# Create your models here.



class Review(core_models.TimeStampedModel):
    """
    Review Model Definition
    """

    review = models.TextField()
    cleanliness = models.IntegerField()
    accuracy = models.IntegerField()
    check_in = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return  f'{self.review} --- {self.room}'