# I can solve cubics with 3 real roots i.e. ax^3+bx^2+cx+d=0.
print("-" * 65)
print("I can solve cubics with 3 real roots i.e. ax^3+bx^2+cx+d=0.")
print("-" * 65)

name = input("What is your name?")
a = int(input("What is your a?"))
b = int(input("What is your b?"))
c = int(input("What is your c?"))
d = int(input("What is your d?"))
b1 = ((-b**3)/27*(a**3))+((b*c)/6*a*a)-(d/(2*a))
b2 = ((c/(3*a))-((b*b)/(9*(a*a))))**3
x = ((((b1*b1)+b2)**0.5)+b1)**(1/3) + (b1-(((b1*b1)+b2)**0.5))**(1/3) - (b/(3*a))

print("Hello", name.capitalize() + ", I will solve", end=" ")

match a:
    case 1:
        print("x^3", end="")
    case -1:
        print("-x^3", end="")
    case 0:
        print(" ", end="")
    case _:
        print(str(a) + "x^3", end="")

match b:
    case 1:
        print("+x^2", end="")
    case -1:
        print("-x^2", end="")
    case 0:
        print(" ", end="")
    case _ if b > 0:
        print("+" + str(b) + "x^2", end="")
    case _ if b < 0:
        print(str(b) + "x^2", end="")

match c:
    case 1:
        print("x", end="")
    case -1:
        print("-x", end="")
    case 0:
        print("", end="")
    case _ if c > 0:
        print("+" + str(c) + "x", end="")
    case _ if c < 0:
        print(str(c) + "x", end="")

match d:
    case 0:
        print("", end="")
    case _ if d > 0:
        print("+" + str(d), end="")
    case _ if d < 0:
        print(d, end="")

print("=0.\n", end="")
print("The root of the cubic is", x.real)

quit()
