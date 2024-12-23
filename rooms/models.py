from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as User_Model


# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """
    Abstract Item model
    """
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """
    Room Type model
    """

    class Meta:
        verbose_name = "Room Type"
        verbose_name_plural = "Room Types"


class Amenity(AbstractItem):
    """
    Amenity model Definition
    """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """
    Facility model Definition
    """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """
    House Rule model Definition
    """

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampedModel):
    """
    Photo model Definition
    """
    caption = models.CharField(max_length=255)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Room(AbstractItem):
    """
    Room model
    """
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    guest = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instance_booked = models.BooleanField(default=False)
    host = models.ForeignKey(User_Model.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
