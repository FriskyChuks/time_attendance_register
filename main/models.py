from django.db import models
from django.contrib.auth.models import User


class ClockInClockOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(blank=False,null=False)
    clock_out = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        if self.clock_out:
            return f"{self.user} -- In: {self.clock_in} || Out: {self.clock_out}"
        return f"{self.user} -- In: {self.clock_in}"
