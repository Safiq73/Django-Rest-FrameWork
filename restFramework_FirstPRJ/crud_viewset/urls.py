
from django.urls import path, include
# from api import views
from . import views
from rest_framework.routers import DefaultRouter

# creating router object
router =DefaultRouter()

# registering StudentViewSet class from views.py
router.register('studentapi', views.StudentViewSet, basename='student')
# Here the URL will be  http://127.0.0.1:8000/crud_viewset/studentapi/
# crud_viewset from main url
# studentapi from this url

urlpatterns = [
    path('', include(router.urls)),
]
