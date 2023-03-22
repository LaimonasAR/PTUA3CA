# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate
# In this class, create the method taste():
#     It will take in a food name as a string.
#     Return {person_name} eats the {food_name}.
#     If the food is in the person's like list, add 'and loves it!' to the end.
#     If it is in the person's hate list, add 'and hates it!' to the end.
#     If it is in neither list, simply add an exclamation mark to the end.
#     p1 = Person("Sam", ["ice cream"], ["carrots"])
#     p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#     p1.taste("cheese") ➞ "Sam eats the cheese!"
#     p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

from typing import List

class Person():

    def __init__(self, name: str, liked_foods: List[str], hated_foods: List[str]) -> None:
        self.name = name
        self.liked_foods = liked_foods
        self.hated_foods = hated_foods

    def taste(self, food: str) ->None:
        suffix = "!"
        if food in self.liked_foods:
            suffix = " and loves it!"
        if food in self.hated_foods:
            suffix = " and hates it!"
        print(f"{self.name} eats {food}{suffix}")


p1 = Person(name = "Antanas", liked_foods=["Burger", "Steak", "Chili"], hated_foods= ["Fish", "Mussels", "Shrimp"])

p1.taste("Shrimp")

p1.taste("Burger")

p1.taste("Mushroom")

