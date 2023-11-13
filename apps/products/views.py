from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.products.permissions import ProductPermission

# Create your views here.
class ProductViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ProductPermission(), )
        return (AllowAny(), )