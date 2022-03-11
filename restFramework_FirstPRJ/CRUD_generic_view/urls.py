
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LCgen_API.as_view() ),
    path('<int:pk>/', views.RUDgen_API.as_view())
]

