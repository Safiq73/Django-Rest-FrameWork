
from django.urls import path, include
# from api import views
from . import views

urlpatterns = [
    path('register', views.register , name='register'),
    path('check', views.check  , name='check'),
    path('users', views.users , name='users'),
    path('users/<int:id>', views.singleUsers , name='singleUsers'),
    path('users/<int:id>/<str:query>', views.query , name='query'),
]
