import requests


response = requests.get("https://httpbin.org/delay/3", timeout = 5)
print(response.json())
assert response.status_code == 200 , "Status Code doesn't match"

response = requests.get("https://httpbin.org/delay/5", timeout = 3)
print(response.json())
#assert response.status_code == 200 , "Status code doesn't match"