from django.http import JsonResponse

from .models import User


def list_users(request):
    users = User.objects.values('uuid', 'email', 'createdAt', 'updatedAt', 'userType')
    return JsonResponse(list(users), safe=False)
