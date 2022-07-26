from django.urls import path

from .views import MyObtainTokenPairView, RegisterView

from rest_framework_simplejwt.views import (
    TokenRefreshView
)


urlpatterns = [
    path('blog/api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('blog/api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blog/api/register/', RegisterView.as_view(), name='register_user'),
]
