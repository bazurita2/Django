from rest_framework import viewsets
from .serializer import UserSerializer
from .models import Usercrud

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Usercrud.objects.all()
    serializer_class = UserSerializer
