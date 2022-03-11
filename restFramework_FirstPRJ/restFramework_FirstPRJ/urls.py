"""restFramework_FirstPRJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from api import views
# from de_serialization import views
# from rest_update import views
from rest_delete import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentInfo/', views.studentDetails),
    # path('deSerialization/', views.studentCreate),
    # path('update/', views.update),
    path('delete/', views.delete),
    path('task1/', include('task1.urls')),
    path('studentInfo/', include('api.urls')),
    path('deSerialization/', include('de_serialization.urls')),
    path('update/', include('rest_update.urls')),
    path('delete/', include('rest_delete.urls')),
    path('crud_fxn_apiView/', include('CRUD_fnxn_api_view.urls')),
    path('CRUD_generic_view/', include('CRUD_generic_view.urls')),
    path('concrete_view/', include('concrete_view.urls')),
    path('task2/', include('task2.urls')),
    path('crud_viewset/', include('crud_viewset.urls')),
    path('crud_model_viewset/', include('crud_model_viewset.urls')),
    path('bsic_authentication/', include('bsic_authentication.urls')),
    path('auth_token/', include('auth_token.urls')),
    path('jwt_authentication/', include('jwt_authentication.urls')),
    path('throtttling/', include('throtttling.urls')),
    path('filtring/', include('filtring.urls')),
    path('paginationn/', include('paginationn.urls')),
    path('serializer_relations/', include('serializer_relations.urls')),
]
