# A program that solves the quadratic equation with one or more real roots.

# A function calculate b^2-4ac
def F(a1, b1, c1):
    return (b1 * b1) - (4 * a1 * c1)

# A function calculate Quadratic1
def quadratic1(a2, b2, c2):
    return (-b2 + (F(a2, b2, c2) ** 0.5)) / (2 * a2)

# A function calculate Quadratic2
def quadratic2(a3, b3, c3):
    return (-b3 - (F(a3, b3, c3) ** 0.5)) / (2 * a3)

# Title
print("I can solve ax^2+bx+c=0 for you!")

# A loop to determine if a is 0? and quadratic have real roots? and real number?
while True:
    try:
        # Input of a b c
        a = float(input("Please give me the 'a' coefficient:"))
        b = float(input("Please give me the 'b' coefficient:"))
        c = float(input("Please give me the 'c' coefficient:"))
        # a = 0?
        if a == 0:
            print("Sorry, but 'a' cannot be zero.")
        # not have real roots
        elif F(a, b, c) < 0:
            print("Sorry, but that quadratic does not have real roots")
        # one real root
        elif F(a, b, c) == 0:
            print("Thank you, that is a valid input :) OKAY I'LL SOLVE IT NOW.")
            print("Root :", quadratic1(a, b, c))
            break  # Exit loop
        # two real roots
        elif F(a, b, c) > 0:
            print("Thank you, that is a valid input :) OKAY I'LL SOLVE IT NOW.")
            print("Root 1:", quadratic1(a, b, c))
            print("Root 2:", quadratic2(a, b, c))
            break  # Exit loop
    # Not a real number
    except:
        print("That is not a real number!")

# End
quit()
