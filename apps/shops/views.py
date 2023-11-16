from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from apps.shops.models import Shop
from apps.shops.serializers import ShopSerializer
from apps.shops.permissons import ShopPermission

# Create your views here.
class ShopViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Shop.objects.all() #Django ORM. SELECT * FROM shops_shop;
    serializer_class = ShopSerializer

    def get_permissions(self):
        print(self.action)
        if self.action in ("update", "partial_update", "destroy"):
            return (ShopPermission(), )
        return (AllowAny(), )
