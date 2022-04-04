from django.db import models
from django.db import transaction

# Create your models here.


class Location(models.Model):
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)

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
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

    @classmethod
    def persist(cls, params):
        location_data = params.pop('location', {})
        with transaction.atomic():
            location = Location(**{k: v for k,v in location_data.items()})
            location.save()
            survivor = Survivor(**{k: v for k,v in params.items()}, location_id=location.id)
            survivor.save()
            return survivor


    def update(self, params):
        for key, value in params.items():
            if key in ['location', 'is_infected']:
                if key == 'location':
                    location = self.location
                    for k, v in value.items():
                        setattr(location, k, v)
                    location.save()
            setattr(self, key, value)
        self.save()