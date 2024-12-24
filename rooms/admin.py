from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


# Register your models here.

class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Info", {'fields': ['name', 'description', 'country', 'city', 'address', 'price']}),
        (
            "Times", {"fields": ['check_in', 'check_out', 'instance_booked']}
        ),
        (
            "Spaces", {"fields": ['guest', 'beds', 'bedrooms', 'baths']}
        ),
        (
            "More about the spaces", {'fields':
                                          ['amenities', 'facilities', 'house_rules']}
        ),
        (
            "Last Details", {'fields': ['host', 'room_type']}
        )
    ]

    inlines = [PhotoInline]

    list_display = ['name', 'country', 'city', 'price', 'guest', 'bedrooms', 'baths', 'check_in', 'check_out',
                    'check_out','total_rating' ]

    list_filter = ['instance_booked', 'city', 'country', 'guest']

    search_fields = ['name', 'city', 'country', 'guest']

    filter_horizontal = ['amenities', 'facilities', 'house_rules']

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_facilities(self, obj):
        return obj.facilities.count()

    def count_house_rules(self, obj):
        return obj.house_rules.count()


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'used_by']

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'used_by']

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['caption', 'get_thumbnail']


    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" height="50px" src="{obj.file}"/>')

    get_thumbnail.short_description = 'Thumbnail'




@admin.register(models.HouseRule)
class HouseRuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'used_by']

    def used_by(self, obj):
        return obj.rooms.count()
