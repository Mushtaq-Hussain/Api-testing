import requests


response = requests.get("https://the-internet.herokuapp.com/basic_auth", auth = ('asd', 'asd'))
print(response.status_code)

response = requests.get("https://the-internet.herokuapp.com/basic_auth", auth = ('admin', 'admin'))
print(response.status_code)