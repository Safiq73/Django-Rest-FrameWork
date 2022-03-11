
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListProductDetails.as_view() ),
    # path('', views.CreateProductDetails.as_view() ),
    # path('<int:pk>/', views.RetrieveProductDetails.as_view())
    # path('<int:pk>/', views.UpdateProductDetails.as_view())
    path('<int:pk>/', views.DestroyProductDetails.as_view())
    # didn't tested all the url patterns, 
]

