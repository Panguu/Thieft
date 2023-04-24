from django.db import models
from authentication.models import User

# Create your models here.
class TrackerManager(models.Model):
    def create_tracker(self, lat, long, gcd, accelerometer_displacement, trackerType):
        tracker = Tracking(
            latitude=lat,
            longitude=long,
            gcd=gcd,
            accelerometer_displacement=accelerometer_displacement,
            trackerType=trackerType
        )
        tracker.save()
        return tracker
    def get_journeyInfo_location(self, journey):
        lastLocation = journey.trackings.all()
        journeytrackings = dict()
        for index, location in enumerate(lastLocation):
            journeytrackings[index] = {'latitude': location.latitude, 'longitude': location.longitude, 'timestamp': location.timestamp, 'gcd': location.gcd, 'accelerometer_displacement': location.accelerometer_displacement, 'trackerType': location.trackerType}
        return journeytrackings


class Tracking(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    gcd = models.FloatField()
    accelerometer_displacement = models.FloatField()
    trackerType = models.CharField(max_length=10, default='Unknown')
    
    def __str__(self):
        return str(self.latitude) + " " + str(self.longitude) + " " + str(self.timestamp) + " " + str(self.gcd) + " " + str(self.accelerometer_displacement)
    
class Journey(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    trackings = models.ManyToManyField(Tracking)

    def __str__(self):
        return str(self.trackings.all())