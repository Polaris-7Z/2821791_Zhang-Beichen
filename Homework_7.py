# I can solve cubics with 3 real roots i.e. ax^3+bx^2+cx+d=0.
def x(a, b, c, d):
    b1 = ((-b ** 3) / 27 * (a ** 3)) + ((b * c) / 6 * a * a) - (d / (2 * a))
    b2 = ((c / (3 * a)) - ((b * b) / (9 * (a * a)))) ** 3
    xx = ((((b1 * b1) + b2) ** 0.5) + b1) ** (1 / 3) + (b1 - (((b1 * b1) + b2) ** 0.5)) ** (1 / 3) - (b / (3 * a))
    return xx

print("-" * 65)
print("I can solve cubics with 3 real roots i.e. ax^3+bx^2+cx+d=0.")
print("-" * 65)

name = input("What is your name?")
A = int(input("What is your a?"))
B = int(input("What is your b?"))
C = int(input("What is your c?"))
D = int(input("What is your d?"))


print("Hello", name.capitalize() + ", I will solve", end=" ")

match A:
    case 1:
        print("x^3", end="")
    case -1:
        print("-x^3", end="")
    case 0:
        print(" ", end="")
    case _:
        print(str(A) + "x^3", end="")

match B:
    case 1:
        print("+x^2", end="")
    case -1:
        print("-x^2", end="")
    case 0:
        print(" ", end="")
    case _ if B > 0:
        print("+" + str(B) + "x^2", end="")
    case _ if B < 0:
        print(str(B) + "x^2", end="")

match C:
    case 1:
        print("x", end="")
    case -1:
        print("-x", end="")
    case 0:
        print("", end="")
    case _ if C > 0:
        print("+" + str(C) + "x", end="")
    case _ if C < 0:
        print(str(C) + "x", end="")

match D:
    case 0:
        print("", end="")
    case _ if D > 0:
        print("+" + str(D), end="")
    case _ if D < 0:
        print(D, end="")

print("=0.\n", end="")
print("The root of the cubic is", x(A, B, C, D).real)

quit()
