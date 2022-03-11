from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# from api.serializers import StudentSerializers
from .serializers import StudentDetailSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def studentCreate(request):
    if request.method =='POST':
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        serializer=StudentDetailSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Your details has been saved'}
            return JsonResponse(res, safe=True)
        jsonData=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application/json')