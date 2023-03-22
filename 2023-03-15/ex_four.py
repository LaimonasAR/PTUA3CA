class A:
    def __init__(self) -> None:
        pass

    def say_hello(self):
        print("Hello from class A")


class B(A):
    def __init__(self) -> None:
        pass
        super().__init__()

    # def say_hello(self):
    #     print("Hello from class B")


class C:
    def __init__(self) -> None:
        pass

    def say_hello(self):
        print("Hello from class C")


object_of_class_c = C()

object_of_class_c.say_hello()

object_of_class_b = B()

object_of_class_b.say_hello()
