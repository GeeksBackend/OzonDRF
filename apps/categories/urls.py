from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryViewSet

router = DefaultRouter()
router.register('', CategoryViewSet, "api_category")

urlpatterns = router.urls