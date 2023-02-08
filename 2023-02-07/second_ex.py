priv_user = ["Tomas", "Laimonas", "Petras"]

my_name = input("Enter Your name: ")

if my_name in priv_user:
    print(f"Welcome, dear {my_name}")
else:
    print("Welcome othervise")