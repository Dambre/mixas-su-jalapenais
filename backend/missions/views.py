from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from .models import Mission, Bid



def all_missions(request):
    _missions = Mission.objects.values('uuid', 'title', 'description', 'creator', 'createdAt', 'updatedAt')
    _missions.order_by('-updatedAt')
    return JsonResponse(list(_missions), safe=False)


# customer calls
def create_mission(request):
    # TODO: post create mission
    pass

def get_mission(request, id):
    _mission = Mission.objects.get(pk=id)
    _mission = _mission.as_dict()

    # append workers bids
    return JsonResponse(_mission, safe=False)


def select_worker(request, id):
    pass


def finish_mission(request):
    pass


# //////////////////////////////////////////////////////
# worker calls

def proposed_missions(request, id):
    _missions = []
    for mission in Mission.objects.get.filter(specialist=request.User):
        _missions.append(mission.as_dict())
    return JsonResponse(_missions, safe=False)


def accept_mission(request, id):
    _mission = get_object_or_404(Mission, pk=id)
    _mission.specialist_approved = True
    _mission.save()
    
    return get_mission(request, id)


def finish_mission(request, id):
    _mission = get_object_or_404(Mission, pk=id)
    _mission. aproved by worker = True #TODO: WRITE THIS RIGHT
    _mission.save()

    return get_mission(request, id)