
from django.urls import path, include
# from api import views
from . import views
from rest_framework.routers import DefaultRouter


router =DefaultRouter()

# registering StudentViewSet class from views.py
router.register('singer', views.SingerModelViewSet, basename='singer')
router.register('song', views.SongModelViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls)),
]
