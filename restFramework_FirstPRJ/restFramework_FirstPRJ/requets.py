# import requests
# URL="http://127.0.0.1:8000/studentInfo/"
# r=requests.get(url=URL)
# data=r.json()
# print(data)

# import requests
# import json
# URL="http://127.0.0.1:8000/deSerialization/"
# data={
#     'name':'safsdjj', 
#     'id':8, 
#     'city':'mnsdklsl'
# }
# json_data=json.dumps(data)
# r=requests.post(url=URL, data=json_data)
# resp=r.json()
# print(resp)

# import requests
# import json
# URL="http://127.0.0.1:8000/update/"
# data={
#     'name':'ui234', 
#     'id':1, 
#     'city':'Punjab'
# }
# json_data=json.dumps(data)
# r=requests.put(url=URL, data=json_data)
# resp=r.json()
# print(resp)

# import requests
# import json
# URL="http://127.0.0.1:8000/crud_fxn_apiView/"
# data={
#     'id':1, 
#     # 'name':'safsdjj', 
#     # 'rollNum':1, 
#     # 'city':'mnsdklsl'
# }
# json_data=json.dumps(data)
# header={'content-Type':'application/json'}
# r=requests.delete(url=URL, data=json_data , headers=header)
# resp=r.json()
# print(resp) 

# import requests 
# import json
# URL="http://127.0.0.1:8000/delete/"
# data={
#     'id':1, 
# }
# json_data=json.dumps(data)
# r=requests.delete(url=URL, data=json_data)
# resp=r.json()
# print(resp)


# import requests
# import json
# URL="http://127.0.0.1:8000/task2/register"
# data={
#     "email":"shafiq@shafiq23.com",
#     "password":"shafiq123",
#     "name":"shafiq",
#     "salary":"1938" ,
#     "department":"Chaiwala",
# }
# json_data=json.dumps(data)
# header={'content-Type':'application/json'}
# r=requests.post(url=URL, data=json_data , headers=header)
# resp=r.json()
# print(resp) 

# import requests
# import json
# URL="http://127.0.0.1:8000/task2/login"
# data={
#     "email":"shafiq@shafiq23.com",
#     "password":"shafiq123",
# }
# json_data=json.dumps(data)
# header={'content-Type':'application/json'}
# r=requests.get(url=URL, data=json_data , headers=header)
# resp=r.json()
# print(resp) 

# import requests
# import json
# URL="http://127.0.0.1:8000/task2/startswith"
# data={
#     "char":"A",
# }
# json_data=json.dumps(data)
# header={'content-Type':'application/json'}
# r=requests.get(url=URL, data=json_data , headers=header)
# resp=r.json()
# print(resp) 

json_data=[{"id":1,"first_name":"Cynthy","last_name":"Tansly","email":"ctansly0@usgs.gov","gender":"Male"},
{"id":2,"first_name":"Goldarina","last_name":"Reymers","email":"greymers1@trellian.com","gender":"Female"},
{"id":3,"first_name":"Monty","last_name":"Lepick","email":"mlepick2@etsy.com","gender":"Female"},
{"id":4,"first_name":"Alastair","last_name":"Gregory","email":"agregory3@wordpress.com","gender":"Male"},
{"id":5,"first_name":"Tania","last_name":"Baudasso","email":"tbaudasso4@ocn.ne.jp","gender":"Female"},
{"id":6,"first_name":"Brooks","last_name":"McCarthy","email":"bmccarthy5@webeden.co.uk","gender":"Female"},
{"id":7,"first_name":"Casie","last_name":"Coop","email":"ccoop6@independent.co.uk","gender":"Female"},
{"id":8,"first_name":"Jasun","last_name":"Collyear","email":"jcollyear7@ucoz.com","gender":"Female"},
{"id":9,"first_name":"Shirlene","last_name":"Poyle","email":"spoyle8@google.de","gender":"Male"},
{"id":10,"first_name":"Kalinda","last_name":"McFall","email":"kmcfall9@php.net","gender":"Male"},
{"id":11,"first_name":"Miller","last_name":"Brabbins","email":"mbrabbinsa@deviantart.com","gender":"Male"},
{"id":12,"first_name":"Ambrosio","last_name":"Leroux","email":"alerouxb@domainmarket.com","gender":"Male"},
{"id":13,"first_name":"Bibby","last_name":"Gourley","email":"bgourleyc@guardian.co.uk","gender":"Agender"},
{"id":14,"first_name":"Fredric","last_name":"Mayzes","email":"fmayzesd@arstechnica.com","gender":"Female"},
{"id":15,"first_name":"Barrie","last_name":"Heckle","email":"bhecklee@mac.com","gender":"Male"},
{"id":16,"first_name":"Lenard","last_name":"Boxall","email":"lboxallf@usda.gov","gender":"Male"},
{"id":17,"first_name":"Deb","last_name":"MacClay","email":"dmacclayg@ehow.com","gender":"Female"},
{"id":18,"first_name":"Franciska","last_name":"Rubinowitch","email":"frubinowitchh@illinois.edu","gender":"Male"},
{"id":19,"first_name":"Blair","last_name":"Wandless","email":"bwandlessi@edublogs.org","gender":"Female"},
{"id":20,"first_name":"Conroy","last_name":"Chasles","email":"cchaslesj@psu.edu","gender":"Male"}]

import requests
import json
URL="http://127.0.0.1:8000/paginationn/"
for i in json_data:
    print(i)
    data=i
    json_data=json.dumps(data)
    header={'content-Type':'application/json'}
    r=requests.post(url=URL, data=json_data , headers=header)
    resp=r.json()
    print(resp) 


