class Country:

    def __init__(self, country:str, popul: int, area: int) -> "Country":
        self.country = country
        self.popul = popul
        self.area = area

    def is_big(self):
        if self.popul > 25000000 or self.area >3000000:
            big = True
        else:
            big = False
        return big
    
    def compare_pd(self, other_country)-> str:

        if self.popul/self.area > other_country.popul/other_country.area:
            result = f"{self.country} has a higher density than {other_country.country}"
        else:
            result = f"{other_country.country} has a higher density than {self.country}"
        return result


australia = Country("Australia", 2354550000, 7692024)
andorra = Country("Andorra", 76098, 468)

print(andorra.compare_pd(australia))
print(andorra.is_big())