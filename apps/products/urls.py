from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet


router = DefaultRouter()
router.register('', ProductViewSet, "api_product")

urlpatterns = router.urls