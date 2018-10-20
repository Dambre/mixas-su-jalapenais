
from rest_framework import generics

from .serializers import UserSerializer
from .models import User


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def create(request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
