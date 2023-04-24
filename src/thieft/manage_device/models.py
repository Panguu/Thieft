from django.db import models
from authentication.models import User
from tracker.models import Journey

# Create your models here.

class BluetoothDevice(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)

class DeviceSettings(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    texting_timeout = models.IntegerField()
    update_journey_interval = models.IntegerField()
    journeys =  models.ManyToManyField(Journey)
    bluetooth_in_range = models.ManyToManyField(BluetoothDevice)
    registeredBluetoothDevices = models.ManyToManyField(BluetoothDevice, related_name='registeredBluetoothDevices')


