"""Write a terminal program that required user to login. 
If user does not have an account he should register. 
credentials are username and password. Store the information in the file txt or pickle. 
Validate user credentials from the file. Once user has logged in: print text: "Hello, <username>". """

from dotenv import load_dotenv


import os
import json

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)
print(env_path)

# users = {
#     "user1": {"username": "user1_username", "password": "user1_password"},
#     "user2": {"username": "user2_username", "password": "user2_password"},
#     "user3": {"username": "user3_username", "password": "user3_password"},
# }

# with open(env_path, "w") as f:
#     json.dump(users, f)


with open(env_path, "r") as f:
    users = json.load(f)

# print(users)

# for user_name in users.items():
#     print(user_name)
#     for name in user_name[1]:
#         print(name)

for user_name in users.values():
    print(user_name)
    if user_name["username"] == "Laimonas":
        print("User Found")
    else:
        print("User Not found")
        # append new user

    # for name in user_name[1]:
    #     print(name)

# creds = json.loads({"username": os.getenv("USERNAME")})


# print(creds)
