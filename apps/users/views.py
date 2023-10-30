from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from apps.users.models import User
from apps.users.serializers import UserSerializer

# Create your views here.
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer