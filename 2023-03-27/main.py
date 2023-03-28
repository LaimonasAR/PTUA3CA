class MyString:
    def __init__(self, value: str):
        self.value = value

    def add_exclamation(self) -> "MyString":
        self.value += "!"
        return self

    def make_upper(self) -> "MyString":
        self.value = self.value.upper()
        return self

    def get_self_value(self) -> str:
        return self.value


my_string = MyString("hello")
# my_string.add_exclamation().make_upper()

print(my_string.value)  # output: "HELLO!"
print(my_string.get_self_value())
