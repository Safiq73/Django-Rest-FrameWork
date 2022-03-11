from functools import partial
import imp
from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializations import EmployeeSerialization
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Create your views here.
@csrf_exempt
def update(request):
    if request.method =='PUT':
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        id=pythonData.get('id')
        stu=Employee.objects.get(id=id)
        print(id)
        print(pythonData)
        serializer=EmployeeSerialization(stu, data=pythonData, partial=True)  # partial is need whenever you want to update partially if don't mention partial then you will have to pass all the values else you will validation error
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Successfully updated'}
            return JsonResponse(res, safe=True)
        jsonData=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application/json')