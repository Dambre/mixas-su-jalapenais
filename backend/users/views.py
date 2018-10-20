from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from .models import User
from .serializers import UserSerializer


def list_users(request):
    # optional
    users = []
    for user in User.objects.all():
        users.append(user.as_dict())

    return JsonResponse(users, safe=False)


def user_by_id(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        data = UserSerializer(request.data)
        if data.is_valid():
            for key, value in data.validated_data.items():
                setattr(user, key, value)

            user.save()

    response = JsonResponse(user.as_dict())
    return response
