from django.shortcuts import render
from .serializers import ProductDetailsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductDetails
from rest_framework.throttling import ScopedRateThrottle


# separate class for each method
# here pk will be handled internally
class ListProductDetails(ListAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='liststu'
    
class CreateProductDetails(CreateAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='createstu'
    
class RetrieveProductDetails(RetrieveAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='retrievestu'
    
class UpdateProductDetails(UpdateAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    
class DestroyProductDetails(DestroyAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    
class ListCreateProductDetails(ListCreateAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    # we can do entire crud operation using ListCreateAPIView and RetrieveUpdateDestroyAPIView
    
class RetrieveUpdateProductDetails(RetrieveUpdateAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    
class RetrieveDestroyProductDetails(RetrieveDestroyAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer
    
class RetrieveUpdateDestroyProductDetails(RetrieveUpdateDestroyAPIView):
    queryset=ProductDetails.objects.all()
    serializer_class=ProductDetailsSerializer