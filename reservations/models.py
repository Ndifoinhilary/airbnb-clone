from django.db import models
from django.utils import timezone

from core import models as core_models


# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """
    Reservation model Definition
    """
    STATUS_PENDING = "PENDING"
    STATUS_CONFIRMED = "CONFIRMED"
    STATUS_CONCEALED = "CONCEALED"
    STATUS_REJECTED = "REJECTED"
    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CONCEALED, "Concealed"),
        (STATUS_REJECTED, "Rejected"),
    )
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    check_in = models.DateField("Check In")
    check_out = models.DateField("Check Out")
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reservations")
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name="reservations")

    def __str__(self):
        return f'{self.room} - {self.check_in} - {self.check_out}'

    def in_progress(self):
        now = timezone.now().date()
        return self.check_in <= now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now >= self.check_out

    is_finished.boolean = True


    def not_started(self):
        now = timezone.now().date()
        return self.check_in > now
    not_started.boolean = True
