# class Numbers:
#     def __init__(self, number: int) -> None:
#         self.number = number

#     @classmethod
#     def get_primes(cls, number: int) -> "Numbers":
#         primes_list = []
#         i = 0
#         while i <= number:


#             for k in range(2, i):
#                 if (i % k) == 0:
#                     break
#                 primes_list.append(i)
#             i += 1
#         return primes_list


# print(Numbers.get_primes(159))
from typing import List


class MathOperations:


    
    @classmethod
    def is_prime(cls, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @classmethod
    def primes(cls, n: int) -> List[int]:
        primes_list = []
        for i in range(2, n + 1):
            if cls.is_prime(i):
                primes_list.append(i)
        return primes_list


print(MathOperations.primes(159))
