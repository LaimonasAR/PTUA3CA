import json

import requests

r = requests.get(
    "https://raw.githubusercontent.com/robotautas/kursas/master/requests/uzduotis.json"
)
print(r.text)
# response = json.loads(r.text)

# print(response)

with open("data2.json", "w") as file:
    json.dump(r.text, file, indent=2, sort_keys=True)

with open("data2.json", "r") as file:
    data = json.load(file)

print(data)
