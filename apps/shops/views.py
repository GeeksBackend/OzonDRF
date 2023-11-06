from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.shops.models import Shop
from apps.shops.serializers import ShopSerializer

# Create your views here.
class ShopViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Shop.objects.all() #Django ORM. SELECT * FROM shops_shop;
    serializer_class = ShopSerializer