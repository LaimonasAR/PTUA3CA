from models import User
from session import session

user = session.query(User).filter(User.id == "1").one()

for data in user.data:
    print(data)
