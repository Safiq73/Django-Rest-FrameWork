
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# creating router object
# router =DefaultRouter()

# router.register('studentapi', views.StudentModelViewSet, basename='student')


urlpatterns = [
    path('',  views.StudentModelViewSet.as_view() , name='StudentModelViewSet'),
    # path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]
