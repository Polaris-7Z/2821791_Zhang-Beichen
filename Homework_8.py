#  Quadratic Equation
def quadratic1(a, b, c):
    return ((-b) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)

def quadratic2(a, b, c):
    return ((-b) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if ((b ** 2) - (4 * a * c)) > 0:
    print("There are 2 solutions \nThere are ", quadratic1(a,b,c), " and ",quadratic2(a,b,c))
elif ((b ** 2) - (4 * a * c)) == 0:
    print("There is 1 solution \nIt is ", quadratic1(a,b,c))
elif ((b ** 2) - (4 * a * c)) < 0:
    print("No solution")

quit()
