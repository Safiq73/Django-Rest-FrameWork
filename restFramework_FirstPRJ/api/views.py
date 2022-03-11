from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer 
from .models import Student
import json

# Create your views here 123.
def studentDetails(request):
    # st=Student.objects.get(rollNum=2)
    st=Student.objects.filter(rollNum=2)[0]     
    serializer=StudentSerializers(st, many=True)    # # for all students we have to write     st=Student.objects.all()
    json_data=json.dumps(serializer.data)       #  we can write using both the methods  
    # json_data=JSONRenderer().render(serializer.data)    
     # JSONRenderer() will convert the python dictionary to JSON formate
    return HttpResponse(json_data, content_type='application/json')
    # instead above 3 lines we can return the response using JsonResponse
    return JsonResponse(serializer.data, safe=False)


def studentDetails(request):
    # st=Student.objects.get(rollNum=2)
    st=Student.objects.all()  # for all students we have to write
    serializer=StudentSerializers(st, many=True)
    json_data=json.dumps(serializer.data)   
    # json_data=JSONRenderer().render(serializer.data)    
    # return HttpResponse(json_data, content_type='application/json')
    # instead above 3 lines we can return the response using JsonResponse
    return JsonResponse(serializer.data, safe=False)
