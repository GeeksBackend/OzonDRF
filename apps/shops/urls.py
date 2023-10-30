from django.urls import path

from apps.shops.views import ShopListAPIView, ShopCreateAPIView, ShopRetrieveAPIView, ShopUpdateAPIView, ShopDestroyAPIView

urlpatterns = [
    path('', ShopListAPIView.as_view(), name="api_shops"),
    path('create/', ShopCreateAPIView.as_view(), name='api_shops_create'),
    path('<int:pk>/', ShopRetrieveAPIView.as_view(), name='api_shop_retrieve'),
    path('update/<int:pk>/', ShopUpdateAPIView.as_view(), name='api_shop_update'),
    path('destroy/<int:pk>/', ShopDestroyAPIView.as_view(), name='api_shop_destroy')
]