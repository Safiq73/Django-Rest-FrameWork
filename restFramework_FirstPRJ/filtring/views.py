
from .models import Filtring
from .serializers import FiltringSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.
class StudentModelViewSet(ListAPIView):
    queryset=Filtring.objects.all()
    serializer_class=FiltringSerializer
    # def get_queryset(self):
    #     user=self.request.user
    #     return Filtring.objects.filter(passedby=user)
    
    # another method filtering    
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['passedby']

    # search filter
    # filter_backends=[SearchFilter]
    # # search_fields=['rollNum', 'name']
    # search_fields=['^name']  # name which starts with
    # search_fields=['=name']     # name which is exactly equal to 
    
    # ordering filter
    filter_backends=[OrderingFilter] # if you just mention this line you will get the option to order all the rows 
    search_fields=['name'] #By mentioning like this only name is allowed to order you can mention multiple as well
