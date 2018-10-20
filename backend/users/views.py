from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from .models import User
from .serializers import UserSerializer


user_values = ['uuid', 'email', 'createdAt', 'updatedAt', 'userType']


def list_users(request):
    users = User.objects.values(*user_values)
    return JsonResponse(list(users), safe=False)


def user_by_id(request, id):
    if request.method == 'POST':
        data = UserSerializer(request.data)
        if data.is_valid():
            user = get_object_or_404(User, pk=id)
            for key, value in data.validated_data.items():
                setattr(user, key, value)

            user.save()
        response = JsonResponse({'status': 'true', 'message': 'User updated'})

    else:
        user = User.objects.values(*user_values).filter(pk=id).first()
        if not user:
            response = JsonResponse({'status': 'false', 'message': 'User not found'}, safe=False, status=404)

        else:
            response = JsonResponse(user, safe=False)

    return response
