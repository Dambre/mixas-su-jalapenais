from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from missions.models import Mission




def all_missions(request):
    _missions = Mission.objects.values('uuid', 'title', 'description', 'creator', 'createdAt', 'updatedAt')
    _missions.order_by('-updatedAt')

    return JsonResponse(list(_missions), safe=False)

def missions_by_creator(request,id):
    _missions = Mission.objects.values('uuid', 'title', 'description', 'creator', 'createdAt', 'updatedAt')
    _missions = _missions.filter(creator=id)

    return JsonResponse(list(_missions), safe=False)

def mission_by_id(request,id):
    _mission = Mission.objects.get(pk=id)
    _mission = _mission.as_dict()

    return JsonResponse(_mission, safe=False)