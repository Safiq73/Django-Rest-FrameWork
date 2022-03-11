
from django.urls import path, include
# from api import views
from . import views

urlpatterns = [
    path('', views.crud_api_view , name='crud_api_view'),
]
