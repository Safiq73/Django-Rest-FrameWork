
from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

# creating router object
router =DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
]
