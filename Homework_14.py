# A program to calculate the rootfactorial

import math
def rootfactorial(x):
    if not type(x) == int:  # Check that x is an int and raises an error if it is not (Type Error)
        raise TypeError("input is not an integer")
    if x < 0:  # Check that x is positive and raises an error if it is not (Value Error)
        raise ValueError("x is not positive")
    if x > 20:  # Check that x must be less than 20 (Value Error)
        raise ValueError("x is not less than 20")

    return math.sqrt(math.factorial(x))


x = input("x:")

print(rootfactorial(x))

quit()
