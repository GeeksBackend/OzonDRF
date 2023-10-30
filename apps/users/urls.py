from django.urls import path 

from apps.users.views import UserListAPIView, UserRetrieveAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name="api_users"),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name="api_users_detail")
]