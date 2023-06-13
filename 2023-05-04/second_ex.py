import re

class User:
    def __init__(self, password: str) -> None:
        self._password = password

    @property
    def password(self) -> str:
        return self._password

    @property
    def check_password(self) -> bool:
        output = True
        if len(self._password) < 8:
            output = False
        if output is True:
            for char in self._password:
                if char.isupper():
                    output = True
                    break
                else:
                    output = False
        if output is True:
            for char in self._password:
                if char.islower():
                    output = True
                    break
                else:
                    output = False
        if output is True:
            for char in self._password:
                if char.isdigit():
                    output = True
                    break
                else:
                    output = False
        return output

    @password.setter
    def password(self, value: str):
        self._password = value

    @staticmethod
    def is_password_strong(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        return True

my_pass = User("asilas123")

print(my_pass.check_password)

my_pass.password = "Asilas123"

print(my_pass.check_password)
