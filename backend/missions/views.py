from django.shortcuts import render
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

def proposed_missions():
    pass


def accept_mission():
    pass


def finish_mission():
    pass