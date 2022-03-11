
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Teacher
from rest_framework.response import Response
from .serializers import TeacherSerializer
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAdminUser

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([BaseAuthentication])
@permission_classes([IsAdminUser])
def crud_api_view(request):
    if request.method=='GET':
        id=request.data.get('id', None)
        if id is not None:        
            user=Teacher.objects.get(id=id)
            serializer=TeacherSerializer(user)
            return Response(serializer.data , status=status.HTTP_200_OK)
        user=Teacher.objects.all()
        serializer=TeacherSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( {'msg':'Your Data has been saved'} , status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        id=request.data.get('id', None)
        user=Teacher.objects.get(id=id)   
        serializer=TeacherSerializer(user,data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Full successfully updated'}, status=status.HTTP_200_OK)
    
    if request.method=='PATCH':
        id=request.data.get('id', None)
        user=Teacher.objects.get(id=id)   
        serializer=TeacherSerializer(user, partial=True, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial successfully updated'}, status=status.HTTP_200_OK)
        
    if request.method=='DELETE':
        id=request.data.get('id', None)
        user=Teacher.objects.get(id=id)   
        user.delete()
        return Response({'msg':'details successfully deleted'})