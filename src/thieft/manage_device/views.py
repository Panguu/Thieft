from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import BluetoothDevice, DeviceSettings
from authentication.models import User
import json


def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)
# Create your views here.

@csrf_exempt
def getSettings(request, device_id):
    if request.method == 'GET':
        device = DeviceSettings.objects.get(id=device_id)

        return JsonResponse(dict(texting_timeout=device.texting_timeout, phoneNumber=device.user.phoneNumber, update_journey_interval=device.update_journey_interval, registeredBluetoothDevices=device.registeredBluetoothDevices))
    return HttpResponse()

@csrf_exempt
def addDevice(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        device = DeviceSettings(
            user=user,
            texting_timeout=postData['texting_timeout'],
            update_journey_interval=postData['update_journey_interval']
        )
        device.save()
        return HttpResponse(device.id)
    return HttpResponse()

@csrf_exempt
def registerDevice(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        if DeviceSettings.objects.filter(id=postData['device_id']).exists():
            device = DeviceSettings.objects.get(id=postData['device_id'])
            device.user = User.objects.get(token=postData['token'])
            device.save()
            return HttpResponse("OK")
        return HttpResponse("Error no device with id " + postData['device_id'])
    return HttpResponse()

@csrf_exempt
def getDevices(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        devices = DeviceSettings.objects.filter(user=user)
        devicedict = dict()
        for index, device in enumerate(devices):
            devicedict[index] = device.id
        return JsonResponse(devicedict)
    return HttpResponse()

@csrf_exempt
def addBluetoothInRange(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        device = DeviceSettings.objects.get(id=postData['device_id'])
        device.bluetooth_in_range.clear()
        for bluetoothTuple in grouped(postData['bluetooth_in_range'], 2):
            bluetooth = BluetoothDevice(
                name=bluetoothTuple[0],
                mac_address=bluetoothTuple[1],
            )
            bluetooth.save()
            device.bluetooth_in_range.add(bluetooth)
            device.save()
        return HttpResponse("added bluetooth devices")
    return HttpResponseBadRequest("error in request")

@csrf_exempt
def addBluetoothToRegisteredDevices(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        device = DeviceSettings.objects.get(user=user)
        print(postData)
        for bluetoothTuple in grouped(postData['registeredBluetoothDevices'], 2):
            print(bluetoothTuple)
            bluetooth = BluetoothDevice(
                name=bluetoothTuple[0],
                mac_address=bluetoothTuple[1]
            )
            bluetooth.save()
            device.registeredBluetoothDevices.add(bluetooth)
            device.save()
        return HttpResponse("added bluetooth device")
    return HttpResponseBadRequest("error in request")

@csrf_exempt
def removeRegisteredBluetoothDevice(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        device = DeviceSettings.objects.get(id=1)
        for bledevice in device.registeredBluetoothDevices.all():
            if bledevice.mac_address == postData["bluetooth_id"]:
                bledevice.delete()
        device.save()
        return HttpResponse("removed bluetooth device")
    return HttpResponseBadRequest("error in request")

@csrf_exempt
def getBluetoothDevicesInRange(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        device = DeviceSettings.objects.filter(user=user)
        bluetoothDevices = []
        for device in device:
            for bluetoothDevice in device.bluetooth_in_range.all():
                bluetoothDevices.append((bluetoothDevice.id, bluetoothDevice.name, bluetoothDevice.mac_address))
        return HttpResponse(json.dumps(bluetoothDevices))
    return HttpResponseBadRequest("error in request")

@csrf_exempt
def getRegisteredBluetoothDevices(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        device = DeviceSettings.objects.get(user=user)
        print(device.registeredBluetoothDevices.all())
        bluetoothDevices = []
        for bluetoothDevice in device.registeredBluetoothDevices.all():
            print(bluetoothDevice.name, bluetoothDevice.mac_address)
            bluetoothDevices.append((bluetoothDevice.id, bluetoothDevice.name, bluetoothDevice.mac_address))
        return HttpResponse(json.dumps(bluetoothDevices))
    return HttpResponseBadRequest("error in request")