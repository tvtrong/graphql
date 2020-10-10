from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DHT11(models.Model):
    timestamp = models.DateTimeField(
        _("thời gian cập nhật"), auto_now_add=True)
    temperature = models.DecimalField(
        _("Nhiệt độ"), max_digits=3, decimal_places=1)
    humidity = models.DecimalField(_("độ ẩm"), max_digits=3, decimal_places=1)
    #remote_address = models.CharField(_('Ip adress'), max_length=255)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp} Temperature: {self.temperature} Humidity: {self.humidity}"
