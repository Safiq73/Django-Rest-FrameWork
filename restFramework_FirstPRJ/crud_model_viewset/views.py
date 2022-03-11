
from .models import Crud_ModelViewSet
from rest_framework import viewsets
from .serializers import Crud_ModelViewSetSerializer

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Crud_ModelViewSet.objects.all()
    serializer_class=Crud_ModelViewSetSerializer
    
# Create your views here.
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    # This is another class using which we can retrieve and list the data, 
    queryset=Crud_ModelViewSet.objects.all()
    serializer_class=Crud_ModelViewSetSerializer