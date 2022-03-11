import io
from rest_framework.parsers import JSONParser
from .models import EmployeeDelete
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.2
@csrf_exempt
def delete(request):
    if request.method =='DELETE':
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        id=pythonData.get('id')
        stu=EmployeeDelete.objects.get(id=id)
        stu.delete()
        res={'msg':'Successfully deleted'}
        return JsonResponse(res, safe=True)