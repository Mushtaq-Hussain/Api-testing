# CRUD
# Create = POST Request
# Read = GET Request
# Update = PUT/PATCH Request
# DELETE = DELETE Request
# PUT = Update/Replace
# PATCH = Update/Modify

# In PUT Request all properties of the object should be provided while making request
# {
#    "Name":"Mushtaq"
#    "phone": 3022661
#   "City": "Peshawar"
# }
# In PATCH Request Specify the only record that you want to update
# {
#   "City": "Islamabad"
# }
import json

import requests

payload = open("data.json", "r").read()
response = requests.post("https://reqres.in/api/users", data=json.loads(payload))
print(response.json())
assert response.json()["name"] == "morpheus"
assert response.json()["job"] == "leader"
