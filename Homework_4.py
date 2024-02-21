a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

def quadratic1(a,b,c):
    return ((-b) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)

def quadratic2(a,b,c):
    return ((-b) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)

print("Quadratic1 is", quadratic1(a,b,c))

print("Quadratic2 is", quadratic2(a,b,c))
