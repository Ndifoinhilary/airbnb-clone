from django.contrib import admin

from reservations.models import Reservation


# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['room', 'status', 'check_in', 'check_out', 'guest', 'not_started', 'in_progress', 'is_finished']
