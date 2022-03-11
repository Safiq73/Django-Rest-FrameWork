# import requests
# import json
# URL="http://127.0.0.1:8000/task1/register"
# data={
#     'name':'safiq1', 
#     'city':'Mangalore', 
#     'number':914238893
# }
# json_data=json.dumps(data)
# r=requests.post(url=URL, data=json_data)
# resp=r.json()
# print(resp)

# import requests
# import json
# URL="http://127.0.0.1:8000/task1/check"
# data={
#     'name':'safiq1',
# }
# json_data=json.dumps(data)
# r=requests.post(url=URL, data=json_data)
# resp=r.json()
# print(resp)


# import requests
# import json
# URL="http://127.0.0.1:8000/task1/users"
# r= requests.get(url=URL)
# resp=r.json()
# print(resp)

# import requests
# import json
# URL="http://127.0.0.1:8000/task1/users/3"
# r= requests.get(url=URL)
# resp=r.json()
# print(resp)

# import requests
# import json
# URL="http://127.0.0.1:8000/task1/users/1/city"
# r= requests.get(url=URL)
# resp=r.json()
# print(resp)


import requests
import json
URL="http://127.0.0.1:8000/task1/users?id=1"
r=requests.get(url=URL)
resp=r.json()
print(resp)