a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter Your symbol: ")


if c == "*":
    print(f"{a} * {b} equals {a*b}")
elif c == "/":
    print(f"{a} / {b} equals {a/b}")
elif c == "+":
    print(f"{a} + {b} equals {a+b}")
elif c == "-":
    print(f"{a} - {b} equals {a-b}")
else:
    print("This is a simple calculator, not scientific")