import math
def rootfactorial(x):
    if not type(x) == int:
        raise TypeError("input is not an integer")
    if x < 0:
        raise ValueError("x is not positive")
    if x > 20:
        raise ValueError("x is not less than 20")

    return math.sqrt(math.factorial(x))


x = input("x:")

print(rootfactorial(x))

quit()
