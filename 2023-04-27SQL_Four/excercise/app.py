from models import User, Data
from session import session


def register_user(login):
    name = input("Enter name ")
    surname = input("Enter surname ")
    password = input("Enter password ")
    new_user = User(name=name, surname=surname, email=login, password=password)
    session.add(new_user)
    session.commit()
    print("Registered succesfully, now login to get to Your data!")


def add_data(userid):
    data_type = input("Enter data type ")
    attribute = input("Enter data ")
    attribute2 = input("Enter more data ")
    data = Data(
        type=data_type, attribute=attribute, attribute2=attribute2, user_id=userid
    )
    session.add(data)
    session.commit()


def get_data(userid):
    got_data = session.query(User).filter(User.id == userid).one()
    for data in got_data.data:
        print(data)


print("Hi please be patient!")

login = input("Enter Your email ")

user_list = session.query(User).all()
user_exists = False
for user in user_list:
    if user.email == login:
        # user = session.query(User).filter(User.email == login)
        pass_correct = False
        while pass_correct is False:
            user_password = input("Enter password ")
            if user.password == user_password:
                print(f"Hi, {user.name}")
                pass_correct = True
        user_exists = True

if user_exists is False:
    print("You are new User, please register")
    register_user(login)


if user_exists is True and pass_correct is True:
    print("You can now access Your data")
    while True:
        current_user = session.query(User).filter(User.email == login).one()
        selection = input("Type '1' to list Your data, '2' to enter more data ")
        if selection == "1":
            get_data(userid=current_user.id)
        elif selection == "2":
            add_data(userid=current_user.id)
        else:
            print("Be carefull, now You'll have to login again!")
            break
