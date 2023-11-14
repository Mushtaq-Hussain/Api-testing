import requests
import json

Payload = {
    "name": "morpheus",
    "job": "leader"
}
Data = {
    "name": "API",
    "job": "API Testing"
}
Data1 = {
    "name": "Mushtaq"
}

api_json = 'C:\\Users\\Mushtaq.Hussain\\PycharmProjects\\Api_Testing\\api_test\\data.json'


class Api_automation:

    def get_request(self):
        response = requests.get("https://reqres.in/api/users?page=2")
        # print(response.url)
        assert response.url == "https://reqres.in/api/users?page=2", "URL not Matching"
        Json_response = response.json()
        # print(Json_response['total'])
        assert Json_response['total'] == 12, "Total doesn't match"
        # print(Json_response['total_pages'])
        assert Json_response['total_pages'] == 2, "Total Pages doesn't match"
        # print(Json_response["data"][0]["email"])
        assert Json_response["data"][0]["email"] == "michael.lawson@reqres.in", "Email doesn't match"
        assert Json_response["data"][0]["email"].endswith("reqres.in"), "Email format doesn't match"
        # print(response.status_code)
        assert response.status_code == 200, "Status Code doesn't match"

    def post_request(self):
        payload = open(api_json, "r").read()
        response = requests.post("https://reqres.in/api/users", data=json.loads(payload))
        print(response.json())
        assert response.json()["name"] == "morpheus"
        assert response.json()["job"] == "leader"

    def Put_request(self):
        response = requests.put("https://reqres.in/api/users/2", data=Data)
        print(response.json())
        print(response.status_code)
        assert response.json()["name"] == "API"
        assert response.json()["job"] == "API Testing"

    def Patch_request(self):
        response = requests.patch("https://reqres.in/api/users/2", data=Data1)
        print(response.json())
        print(response.status_code)
        assert response.json()["name"] == "Mushtaq"

    def delete_request(self):
        response = requests.delete("https://reqres.in/api/users/2")
        print(response.status_code)
        assert response.status_code == 204

    def invalid_Auth_request(self):
        response = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('asd', 'asd'))
        print(response.status_code)

    def valid_Auth_request(self):
        response = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('admin', 'admin'))
        print(response.status_code)

    def valid_timeout_request(self):
        response = requests.get("https://httpbin.org/delay/3", timeout=5)
        print(response.json())
        assert response.status_code == 200, "Status Code doesn't match"

    def invalid_timeout_request(self):
        response = requests.get("https://httpbin.org/delay/5", timeout=3)
        print(response.json())


