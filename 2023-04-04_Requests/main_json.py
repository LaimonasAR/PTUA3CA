import json

data = """{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price" 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson",
        "status": null,
        "married": true
     } 
  ]   
}"""

data_dict = json.loads(data)
# print(data_dict)
# print(type(data_dict))

with open("example2.json", "w") as file:
    json.dump(data, file, indent=2, sort_keys=True)

with open("example2.json", "r") as file:
    data = json.load(file)

print(data)
