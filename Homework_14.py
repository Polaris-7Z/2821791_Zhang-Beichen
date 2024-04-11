import math
def rootfactorial(x):
    try:
        x = int(x)
    except:
        raise TypeError("x is not and integer")

    if x < 0:
        raise ValueError("x is not positive")
    if x > 20:
        raise ValueError("x is not less than 20")

    return math.sqrt(math.factorial(x))


x = input("x:")

print(rootfactorial(x))

quit()