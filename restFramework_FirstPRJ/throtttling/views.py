
from .models import Throtttling
from rest_framework import viewsets
from .serializers import ThrotttlingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .trottling import Throttle1

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Throtttling.objects.all()
    serializer_class=ThrotttlingSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle, Throttle1]