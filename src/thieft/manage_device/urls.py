from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('device/<int:device_id>', views.getSettings),
    path('device/add/', views.addDevice),
    path('device/getDevices/', views.getDevices),
    path('device/registerDevice/', views.registerDevice),
    path('device/registerBluetooth/', views.addBluetoothToRegisteredDevices),
    path('device/addRangeBluetooth/', views.addBluetoothInRange),
    path('device/getBluetoothDevicesInRange/', views.getBluetoothDevicesInRange),
    path('device/getregisteredBluetoothDevices/', views.getRegisteredBluetoothDevices),
    path('device/setregisteredBluetoothDevices/', views.registerDevice),
    path('device/removeBluetooth/', views.removeRegisteredBluetoothDevice),
    path('device/getSettings/<int:device_id>', views.getSettings),
]