
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# creating router object
router =DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/', TokenObtainPairView.as_view(), name="tokenObtain"),
    path('refreshtoken/', TokenRefreshView.as_view(), name="token_refresh"),
    path('verifytoken/', TokenVerifyView.as_view(), name="token_verify"),
]
