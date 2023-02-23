# my_username = "Laimonas"
# My_pass = "Password"


# check = True
# while check:
#     entered_username = input("Enter Your username: ")
#     entered_pass = input("Enter password: ")
#     if entered_username == my_username and entered_pass == My_pass:
#         print("Uername and pass are correct")
#         check = False


my_creds = ["Laimonas", "SafePass"]
while True:
    my_pass = input("Enter Your username and password: ").split()
    if my_creds[0] == my_pass[0] and my_creds[1] == my_pass[1]:
        break
print("Your credentials are correct")


