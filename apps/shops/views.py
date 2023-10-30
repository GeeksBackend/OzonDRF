from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.shops.models import Shop
from apps.shops.serializers import ShopSerializer

# Create your views here.
class ShopListAPIView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopCreateAPIView(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopRetrieveAPIView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopUpdateAPIView(UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDestroyAPIView(DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer