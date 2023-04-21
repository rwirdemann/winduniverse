from django.db import models


class Spot(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Session(models.Model):
    sport = models.CharField(max_length=200)
    date = models.DateTimeField("date of session")
    spot = models.ForeignKey(Spot, on_delete=models.RESTRICT)

    # distance in meter
    distance = models.FloatField

    # max speed in m/s
    max_speed = models.FloatField

    # duration in minutes
    duration = models.IntegerField

    def __str__(self):
        return f'{self.sport} {self.date}'
