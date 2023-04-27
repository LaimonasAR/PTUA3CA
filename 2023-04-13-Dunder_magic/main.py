# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from typing import List


# class MyList:
#     def __init__(self, items: List[int]) -> None:
#         self.items = items

#     def __bool__(self) -> bool:
#         if len(self.items) < 2:
#             return False
#         return True

#     def __len__(self) -> int:
#         return len(self.items)

#     def __str__(self) -> str:  #graziaia pavadina klases objekta
#         return "My Favorite Class for Lists"


# # my_list = [1,2,3,4,5]
# # print(len(my_list))

# # print(dir(MyList))


# my_list = MyList(items=[1, 2, 3])

# # print(bool(my_list))
# print(my_list)


class MyDict:
    def __init__(self, data: dict):
        self.data = data

    def __str__(self) -> str:
        return "Awesome class"

    def __getitem__(self, key: str):
        return self.data[key]


md = MyDict({"a": 1, "b": 2})

print(md)
print(md.data["a"])
print(md["a"])  # 1
