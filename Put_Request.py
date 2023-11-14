import requests

Data = {
    "name": "API",
    "job": "API Testing"
}

response = requests.put("https://reqres.in/api/users", data=Data)
print(response.json())
assert response.json()["name"] == "API"
assert response.json()["job"] == "API Testing"
