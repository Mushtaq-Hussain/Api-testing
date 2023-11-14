import requests

Payload = {
    "name": "morpheus",
    "job": "leader"
}
Data = {
    "name": "API",
    "job": "API Testing"
}
Data1 = {
    "name": "Mushtaq",

}
response = requests.post("https://reqres.in/api/users", data=Payload)
print(response.json())
print(response.status_code)
assert response.json()["name"] == "morpheus"
assert response.json()["job"] == "leader"


response = requests.put("https://reqres.in/api/users/2", data=Data)
print(response.json())
print(response.status_code)
assert response.json()["name"] == "API"
assert response.json()["job"] == "API Testing"


response = requests.patch("https://reqres.in/api/users/2", data=Data1)
print(response.json())
print(response.status_code)
assert response.json()["name"] == "Mushtaq"

response = requests.delete("https://reqres.in/api/users/2")
print(response.status_code)
assert response.status_code == 204