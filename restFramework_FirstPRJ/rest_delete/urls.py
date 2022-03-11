
from django.urls import path, include
# from api import views
from . import views

urlpatterns = [
    path('', views.delete , name='delete'),
]
