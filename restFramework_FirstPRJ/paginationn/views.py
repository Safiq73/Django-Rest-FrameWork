
from .models import Pgination
from .serializers import PginationSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .mypagination import MyPage

# Create your views here.
class StudentModelViewSet(ListAPIView):
    queryset=Pgination.objects.all()
    serializer_class=PginationSerializer
    pagination_class= MyPage