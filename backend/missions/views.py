from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Mission, Bid
from users.models import User


def all_missions(request):
    _missions = Mission.objects.values('uuid', 'title', 'description', 'creator', 'createdAt', 'updatedAt')
    _missions.order_by('-updatedAt')
    return JsonResponse(list(_missions), safe=False)


# customer calls
def create_mission(request):
    data = request.POST
    mission = Mission.objects.create(creator_id=request.user_id, **data)
    return JsonResponse(mission.as_dict())


def get_mission(request, id):
    mission = Mission.objects.get(pk=id)
    mission = mission.as_dict()
    bids = []
    for bid in Bid.objects.filter(mission_id=mission['uuid']):
        bids.append(bid.as_dict())

    mission.update({'bids': bids})
    return JsonResponse(bids)


def select_worker(request, id):
    data = request.POST
    mission = Mission.objects.get(pk=id)
    mission.worker_id = data.get('worker')
    mission.save()
    return JsonResponse({'success': True})


def finish_mission(request, id):
    mission = Mission.objects.get(pk=id)
    user_type = User.objects.get(user=request.user).userType
    if user_type == 'customer':
        mission.finished_by_customer = True

    elif user_type == 'worker':
        mission.finished_by_worker = True

    mission.save()
    return JsonResponse({'success': True})


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