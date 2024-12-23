from django.contrib import admin
from . import  models
# Register your models here.



@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HouseRule)
class HouseRuleAdmin(admin.ModelAdmin):
    pass