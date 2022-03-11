
from rest_framework.decorators import api_view
from .models import Manager
from rest_framework.response import Response
from .serializers import ManagerSerializer
from rest_framework import status

# Create your views here.
@api_view([ 'POST'])
def register(request):
    if request.method=='POST':
        email=request.data.get('email', None)
        if email is not None:            
            mng=Manager.objects.filter(email=email).first()
            print(mng)
            if mng is None:
                serializer=ManagerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'Your account has been registered'} ,status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg':'Email already exist'} ,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'POST'])
def login(request):
    if request.method=='GET':
        email=request.data.get('email', None)
        password=request.data.get('password', None)
        if email is not None and password is not None:
            mng=Manager.objects.filter(email=email).first()
            if mng is not None:
                Serializer=ManagerSerializer(mng)
                data=Serializer.data
                if password==data.get('password'):
                    return Response({'msg':'Your are successfully logged in'} ,status=status.HTTP_200_OK)
                return Response({'msg':'wrong password'} ,status=status.HTTP_400_BAD_REQUEST)            
            return Response({'msg':'Account doesn\'t exist'} ,status=status.HTTP_400_BAD_REQUEST)            
        
@api_view(['GET', 'POST'])
def startswith(request):
    if request.method=='GET':
        char=request.data.get('char', None)
        if char is not None:
            mng=Manager.objects.filter(name__istartswith=char)
            resp=[]
            if mng is not None:   
                for i in mng:
                    Serializer=ManagerSerializer(i)
                    resp.append(Serializer.data.get('name'))
            return Response(resp, status=status.HTTP_200_OK) 
        return Response({'msg':'No such accounts'} ,status=status.HTTP_400_BAD_REQUEST)
