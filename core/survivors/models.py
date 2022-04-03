from django.db import models

# Create your models here.
class Survivor(models.Model):

    class Meta:
        db_table = 'survivor'

    name = models.CharField(max_length=255, blank=False, null=False)
    age = models.PositiveIntegerField(max_length=255, blank=False, null=False)
    gender = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        choices=(('Male', 'Male'),('Female', 'Female')),
    )
    is_infected = models.BooleanField(blank=False, null=False, default=False)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)