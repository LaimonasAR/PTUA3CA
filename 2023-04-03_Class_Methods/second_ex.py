class Speech:
    def __init__(self, my_string: str) -> None:
        self.my_string = my_string

    @classmethod
    def get_reversed_string(cls, my_string: str) -> "Speech":
        return my_string[::-1]


print(Speech.get_reversed_string("Watafak"))
