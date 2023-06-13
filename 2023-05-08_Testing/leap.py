from typing import List

class Leap:

    def check(self, year: int) -> bool:
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    def range(self, start: int, finish: int) -> List[int]:
        years = []
        for year in range(start, finish):
            if self.check(year):
                years.append(year)
        return years
    
if __name__ == "__main__":
    leap = Leap()
    print(leap.check(2020))

