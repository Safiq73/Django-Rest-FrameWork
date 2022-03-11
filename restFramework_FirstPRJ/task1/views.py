from unicodedata import name
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Users


# Create your views here.
list_of_users=[{"id":1,"first_name":"Gerhard","last_name":"Wethers","email":"gwethers0@google.cn","gender":"Male","city":"Adh Dhayd"},
{"id":2,"first_name":"Ronald","last_name":"Cromly","email":"rcromly1@nydailynews.com","gender":"Female","city":"Manogay"},
{"id":3,"first_name":"Heather","last_name":"Brogan","email":"hbrogan2@mtv.com","gender":"Female","city":"Vrangel’"},
{"id":4,"first_name":"Francoise","last_name":"Wiggin","email":"fwiggin3@wisc.edu","gender":"Male","city":"Velikovechnoye"},
{"id":5,"first_name":"Meaghan","last_name":"Gebb","email":"mgebb4@artisteer.com","gender":"Female","city":"Charlestown"},
{"id":6,"first_name":"Debby","last_name":"Walak","email":"dwalak5@admin.ch","gender":"Female","city":"Bangolo"},
{"id":7,"first_name":"Fergus","last_name":"Legier","email":"flegier6@china.com.cn","gender":"Female","city":"Baisha"},
{"id":8,"first_name":"Bernelle","last_name":"Greatbank","email":"bgreatbank7@ted.com","gender":"Female","city":"Kantemirovka"},
{"id":9,"first_name":"Martita","last_name":"Keirle","email":"mkeirle8@cloudflare.com","gender":"Male","city":"Valeirinha"},
{"id":10,"first_name":"Gray","last_name":"Farrar","email":"gfarrar9@google.nl","gender":"Female","city":"Meijiang"}]
@csrf_exempt
def register(request):
    if request.method=='POST':
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        serializer=UserSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Your details has been registered"}
            return JsonResponse(res, safe=True)
        jsonData=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application/json')

@csrf_exempt
def check(request):
    if request.method=='POST':
        jsonData=request.body
        stream=io.BytesIO(jsonData)
        pythonData=JSONParser().parse(stream)
        allUsers=Users.objects.get(name__icontains=pythonData['name'])
        if len(allUsers.name)>0:
            res={'msg':"Your account exists"}
            return JsonResponse(res, safe=True)
        else:
            res={'msg':"Your account doesn't exist"}
            return JsonResponse(res, safe=True)
def users(request):
    print(request.GET)
    id=request.GET.get('id', False)
    name=request.GET.get('name', False)
    city=request.GET.get('city', False)
    if id==False:
        allUsers=Users.objects.all()
        serializer=UserSerializer(allUsers, many=True)
        jsonData=JSONRenderer().render(serializer.data)
        return HttpResponse(jsonData, content_type='application/json') 
    else:
        if id!=False:
            allUsers=Users.objects.filter(id=id)[0]
            serializer=UserSerializer(allUsers)
            allUsers=serializer.data
        if name!=False and city!=False:
            allUsers={'name':allUsers['name'], 'city':allUsers['city']}
        elif name!=False:
            allUsers={'name':allUsers['name']}
        elif city!=False:
            allUsers={'city':allUsers['city']}        
        return JsonResponse(allUsers, safe=False)
        
        
    # print('req', request)
    # id=request.GET.get('id', '')   
    # id=request.GET['id']
    # id= request.query_params.get('id') 
    # id= request..get('id')
    # name= request.data['name']
    # city= request.data['city']
    # print(id)
    # serializer=UserSerializer(allUsers, many=True)
    # jsonData=JSONRenderer().render(serializer.data)
    # return HttpResponse(jsonData, content_type='application/json') 

def singleUsers(request, id):
    print(id)
    allUsers=Users.objects.filter(id=id)
    if len(allUsers)>0:
        serializer=UserSerializer(allUsers[0])
        jsonData=JSONRenderer().render(serializer.data)
        return HttpResponse(jsonData, content_type='application/json') 
    else:
        res={'msg':"Your account doesn't exist"}
        return JsonResponse(res, safe=True)

def query(request,id,  query):
    allUsers=Users.objects.filter(id=id)
    if len(allUsers)>0:
        print(allUsers[0].city)
        if query=='city':
            jsonData=allUsers[0].city
        elif query=='name':
            jsonData=allUsers[0].name
        elif query=='number':
            jsonData=allUsers[0].number
        return JsonResponse(jsonData, safe=False)

    else:
        res={'msg':"Your account doesn't exist"}
        return JsonResponse(res, safe=True)

    
    
    