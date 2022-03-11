from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Using the mixin methods request method will be processed
# Create your views here.

# List, create - where pk is not required
class LCgen_API(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
# Retrieve, update, destroy- where pk is required
class RUDgen_API(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    # here the object with id pk will be automatically accessed, 
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)