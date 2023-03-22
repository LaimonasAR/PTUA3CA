# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. 
#     If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
#     Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.
from typing import Dict

class Smoothie():

    def __init__(self, ingredients: Dict[str, int]) -> None:
        self.ingredients = ingredients

    def get_cost(self) -> int:
        cost = 0
        for i in self.ingredients.values():
            cost += i
        return cost

    def get_price(self) -> int:
       # self.get_cost()
        cost = self.get_cost()
        price = cost + (cost * 1.5)

        return price
    
    def get_name(self) ->str:
        drink = "Fusion"
        if len(self.ingredients) > 1:
            drink = "Smoothie"
        whats_inside = []
        for i in self.ingredients.keys():
            whats_inside.append(i)
        whats_inside = sorted(whats_inside)
        ingredients = ""
        for ing in whats_inside:
            ingredients += ing + ", "
        sentence = f"{drink} thac contains {ingredients}"
        return sentence


# class TropicalFruit(Smoothie):

#     def __init__(self, ingredients: Dict[str, int]) -> None:
#         self.ingredients = ingredients
#         super().__init__(ingredients=self.ingredients)

# class BerrieMix(Smoothie):

#     def __init__(self, ingredients: Dict[str, int]) -> None:
#         self.ingredients = ingredients
#         super().__init__(ingredients=self.ingredients)

# drink_one = TropicalFruit({"Banana": 5, "Pineapple": 8, "Coconut": 4})

# drink_two = BerrieMix({"Raspberry": 5, "Strawberry": 6, "Blueberry": 9})

# print(f"Tropical fruit dink is a {drink_one.get_name()}, costs {drink_one.get_cost()} and has a price of {drink_one.get_price()}")


class TropicalFruit(Smoothie):

    def __init__(self) -> None:
        self.ingredients = {"Banana": 5, "Pineapple": 8, "Coconut": 4}
        super().__init__(self.ingredients)

class BerrieMix(Smoothie):

    def __init__(self) -> None:
        self.ingredients = ({"Raspberry": 5, "Strawberry": 6, "Blueberry": 9})
        super().__init__(self.ingredients)

smoothis = TropicalFruit()
print(smoothis.get_name())
#print(f"Tropical fruit dink is a {TropicalFruit}, costs {(TropicalFruit.get_cost())} and has a price of {TropicalFruit.get_price}")