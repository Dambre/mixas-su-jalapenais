from django.shortcuts import render
from django.http import JsonResponse
from missions.models import Mission


def all_missions(request):
    Missions = Mission.objects.values('uuid', 'title', 'description', 'creator', 'createdAt', 'updatedAt')
    Missions.order_by('-updatedAt')

    return JsonResponse(list(Missions), safe=False)

# def list_users(request):
#     users = User.objects.values('uuid', 'email', 'createdAt', 'updatedAt', 'userType')
#     return JsonResponse(list(users), safe=False)


def missions_by_creator(request):
    Mission = Mission.objects.filter(creator=request.User)


