from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from authentication.models import User
from manage_device.models import DeviceSettings
import tracker
from .models import Tracking, Journey, TrackerManager
import json


@csrf_exempt
def getJourneyInfo(request, device_id, journey_id):
    if request.method == 'GET':
        device = DeviceSettings.objects.get(id=device_id)
        journey = device.journeys.get(id=journey_id)
        return HttpResponse(journey.trackings.all())
    return HttpResponse("Error method is not GET")

@csrf_exempt
def getAllJourneysForDevice(request):
    if request.method == 'POST':
        user = User.objects.get(token=json.loads(request.body.decode('utf-8'))["token"])
        devices = DeviceSettings.objects.filter(user=user)
        allJourneysVariable = dict()
        for device in devices:
            journey_info = dict()
            for j in device.journeys.all():
                journey_info[j.id] = [{'latitude': t.latitude, 'longitude': t.longitude, 'timestamp': t.timestamp, 'gcd': t.gcd,'accelerometer_displacement': t.accelerometer_displacement, 'trackerType': t.trackerType} for t in j.trackings.all()]
            allJourneysVariable[device.id] = journey_info
        return JsonResponse(allJourneysVariable, safe=False)
    return HttpResponse("Error method is not GET")

@csrf_exempt
def createJourney(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        device = DeviceSettings.objects.get(id=postData['device_id'])
        journey = Journey()
        journey.save()
        device.journeys.add(journey)
        device.save()
        return HttpResponse(journey.id)
    return HttpResponse("Error method is not POST")

@csrf_exempt
def postJourneyInfo(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(username=postData['username'])
        device = DeviceSettings.objects.get(user=user, id=postData['device_id'])
        device_journeys = device.journeys.all()
        journey = device_journeys.get(id=postData['journey_id'])
        trackerType = "Theft" if postData['accelerometer_displacement'] < 60 else "Collision"
        journey.trackings.add(TrackerManager().create_tracker(lat=postData['latitude'], long=postData['longitude'], gcd=postData['gcd'],accelerometer_displacement=postData['accelerometer_displacement'], trackerType=trackerType))
        journey.save()
        device.save()
        return HttpResponse(str(journey))
    return HttpResponse("post Failed")

@csrf_exempt
def getjourneyLocation(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8'))
        user = User.objects.get(token=postData['token'])
        device = DeviceSettings.objects.get(user=user, id=postData['device_id'])

        journey = device.journeys.get(id=postData['journey_id'])
        return JsonResponse(TrackerManager().get_journeyInfo_location(journey))
    return HttpResponse("Error method is not POST")