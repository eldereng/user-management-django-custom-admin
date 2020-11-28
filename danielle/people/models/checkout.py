from django.db import models
from .base import BaseModel
from .checkin import Checkin


class Checkout(BaseModel):
    class Meta:
        verbose_name_plural = "Check-out's"
        verbose_name = "Check-out"

    checkin = models.ForeignKey(Checkin, on_delete=models.PROTECT)

    def __str__(self):
        return self.checkin.person.name + " " + self.created_at.strftime(
            "%d/%m/%Y")
