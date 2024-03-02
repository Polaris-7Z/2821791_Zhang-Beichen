# Output of factorial
def F(x, a):  # Calculate the factorial
    if a == 1 or a == 0:  # If a = 1, give back the result
        return x
    else:
        a -= 1  # reduce a by 1
        x *= a  # multiply x by a
        print("*" + str(a), end="")
        return F(x, a)

# input
n = int(input("Give me a x:"))
# print
print("F(" + str(n) + ")=" + str(n), end="")
print("=" + str(F(n, n)))