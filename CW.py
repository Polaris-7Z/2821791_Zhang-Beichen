# parent class
class quadratic:
    name = "quadratic"
    def __init__(self, a=0.00, b=0.00, c=0.00):
        self.a = a
        self.b = b
        self.c = c
    # sets
    def setA(self, A):
        self.a = A
    def setB(self, B):
        self.b = B
    def setC(self, C):
        self.c = C
    # gets
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def numOfRoots(self):
        if self.a == 0 and self.b != 0:
            return 1
        if self.a == 0 and self.b == 0:
            return 0
        formula = (self.b ** 2) - (4 * self.a * self.c)
        if formula > 0:  # two roots
            return 2
        elif formula == 0:  # one root
            return 1
        else:  # no root
            return 0

    def root1(self):
        if self.numOfRoots() == 0:  # no root
            raise ValueError("No real solution exists")
        elif self.numOfRoots() == 1:  # one root
            if self.a == 0:
                return -self.c / self.b  # bx + c == 0
            return -self.b / (2 * self.a)
        else:  # first root
            formula = (self.b ** 2) - (4 * self.a * self.c)
            return (-self.b + (formula ** 0.5)) / (2 * self.a)

    def root2(self):
        if self.numOfRoots() == 0:  # no root
            raise ValueError("No real solution exists")
        elif self.numOfRoots() == 1:  # one root
            if self.a == 0:
                return -self.c / self.b  # bx + c == 0
            return -self.b / (2 * self.a)
        else:  # second root
            formula = (self.b ** 2) - (4 * self.a * self.c)
            return (-self.b - (formula ** 0.5)) / (2 * self.a)

# child class
class linear(quadratic):
    def __init__(self, b, c):
        super().__init__(0, b, c)

class testEquation():
    # list
    expressions = [
        quadratic(1, 4, 1),
        quadratic(1, 4, 4),
        quadratic(1, 1, 1),
        quadratic(0, 1, 1),
        quadratic(0, 0, 1),
        linear(1, 1),
    ]
    # for loop for print
    for test in expressions:
        try:
            num = test.numOfRoots()
            if isinstance(test, linear):  # if linear
                print(str(test.b) + 'x+' + str(test.c) + " has " + str(num) + " distinct real root(s).")
            else:  # quadratic
                print(str(test.a) + "x**2+" + str(test.b) + 'x+' + str(test.c) + " has " + str(num) + " distinct real root(s).")
            if num == 2:  # two roots
                print("The roots are " + str(test.root1()) + " and " + str(test.root2()))
            if num == 1:  # one root
                print("The root is " + str(test.root1()))
        except ValueError as e:
            print(e)  # ValueError
        print('#' * 35)


# function calling
testEquation()
# End
quit()
