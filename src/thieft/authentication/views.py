from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import User, UserProfile
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getUsers(request):
    if request.method == 'GET':
        users = User.objects.all()
        return HttpResponse(users)
    return HttpResponseBadRequest("Error method is not GET")

@csrf_exempt
def getProfileDetails(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        userProfile = User.objects.get(token=postData['token']).profile
        return JsonResponse({'firstName': userProfile.firstName, 'lastName': userProfile.lastName, 'phoneNumber': userProfile.phoneNumber, 'address': userProfile.address, 'city': userProfile.city, 'country': userProfile.country})
    return HttpResponseBadRequest("Error method is not POST")

@csrf_exempt
def updateProfileDetails(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        user.profile.firstName = postData['firstName']
        user.profile.lastName = postData['lastName']
        user.profile.phoneNumber = postData['phoneNumber']
        user.profile.address = postData['address']
        user.profile.city = postData['city']
        user.profile.country = postData['country']
        user.profile.save()
        return HttpResponse(user.profile)
    return HttpResponseBadRequest("Error method is not POST")

@csrf_exempt
def removeUser(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(username=user_id)
        user.delete()
        return HttpResponse("User with username: " + str(user_id) + " was deleted")
    return HttpResponseBadRequest("Error method is not GET")

@csrf_exempt
def createUser(request, user_id):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        profile = UserProfile()
        profile.save()
        user = User(
            username=user_id,
            profile=profile,
        )
        user.set_password(postData['password'])
        user.save()
        return HttpResponse("User with username: " + str(user_id) + " was created")
    return HttpResponseBadRequest("Error method is not POST")

@csrf_exempt
def changeUsername(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        user.username = postData['new_username']
        user.save()
        return HttpResponse("Username changed to: " + str(postData['new_username']))
    return HttpResponseBadRequest("Error method is not POST")

@csrf_exempt
def changePassword(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=postData['token'])
        user.password = postData['new_password']
        user.save()
        return HttpResponse("Username changed")
    return HttpResponseBadRequest("Error method is not POST")

@csrf_exempt
def checkToken(request):
    if request.method == 'POST':
        postData = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.filter(token=postData['token'])
        if len(user) == 1:
            return HttpResponse("Token is valid")
        return HttpResponse("Token is invalid")
    return HttpResponseBadRequest("Error method is not POST")


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        values = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(username=values['username'])
        user.is_active = True
        user.save()
        return JsonResponse({'token': user.token})
    return HttpResponseBadRequest("Login Failed")

@csrf_exempt
def logoutUser(request):
    if request.method == 'POST':
        values = json.loads(request.body.decode('utf-8').replace("'", '"'))
        user = User.objects.get(token=values['token'])
        user.is_active = False
        user.save()
        return HttpResponse("User with username: " + str(user.username) + " was logged out")
    return HttpResponseBadRequest("Error method is not POST")