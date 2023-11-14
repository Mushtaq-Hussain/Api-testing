import requests

response = requests.get("https://reqres.in/api/users?page=2")
print(response.url)
assert response.url == "https://reqres.in/api/users?page=2", "URL not Matching"
Json_response = response.json()
print(Json_response['total'])
assert Json_response['total'] == 12 , "Total doesn't match"
print(Json_response['total_pages'])
assert Json_response['total_pages'] == 2, "Total Pages doesn't match"
print(Json_response["data"][0]["email"])
assert Json_response["data"][0]["email"] == "michael.lawson@reqres.in", "Email doesn't match"
assert Json_response["data"][0]["email"].endswith("reqres.in") , "Email format doesn't match"
print(response.status_code)
assert response.status_code == 200, "Status Code doesn't match"
