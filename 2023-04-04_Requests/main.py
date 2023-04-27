import requests

# r = requests.get("http://google.com")
# print(r.status_code)

# print(r.text)

# print(dir(r))
import json

data = {"name": "Jonas", "lastname": "Jonaitis"}
r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)
response = json.loads(r.text)
print(type(response))
print(response["form"]["lastname"])
