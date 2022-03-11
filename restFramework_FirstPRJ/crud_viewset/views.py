
from .models import Crud_ViewSet
from rest_framework.response import Response
from .serializers import Crud_ViewSetSerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu=Crud_ViewSet.objects.all()
        Serializer=Crud_ViewSetSerializer(stu, many=True)
        return Response(Serializer.data)
    
    def retrieve(self, request, pk=None):
        if pk is not None:
            stu=Crud_ViewSet.objects.get(id=pk)
            Serializer=Crud_ViewSetSerializer(stu)
            return Response(Serializer.data)
    
    def create(self, request):
        # Here there are arguments which will be inbuilt with viewset class, it wil be valid for all the methods, we can use those methods for further conditions
        print('********Create*************')
        print("BASE NAME", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("NAME", self.name)
        print("Description", self.description)        
        Serializer=Crud_ViewSetSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response( {'msg':'Your Data has been saved'} , status=status.HTTP_200_OK)   
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
 
    def update(self, request, pk=None):
        if pk is not None:
            stu=Crud_ViewSet.objects.get(id=pk)
            Serializer=Crud_ViewSetSerializer(stu, data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                return Response( {'msg':'Your Data has been updated'} , status=status.HTTP_200_OK)   
            return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
 
    def partial_update(self, request, pk=None):
        if pk is not None:
            stu=Crud_ViewSet.objects.get(id=pk)
            Serializer=Crud_ViewSetSerializer(stu, data=request.data, partial=True)
            if Serializer.is_valid():
                Serializer.save()
                return Response( {'msg':'Your Data has been partially updated'} , status=status.HTTP_200_OK)   
            return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
            
    def destroy(self, request, pk=None):
        if pk is not None:
            stu=Crud_ViewSet.objects.get(id=pk)
            stu.delete()
            return Response( {'msg':'Your Data has been deleted'} , status=status.HTTP_200_OK)   
