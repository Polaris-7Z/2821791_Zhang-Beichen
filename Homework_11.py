# A program that requires base and power.

# input
base = int(input("base:"))
power = int(input("power:"))

x = base  # Backup base in x

print(x, end=" ")  # print the base

for a in range(1, power):  # calculate the power, start from 1, end at power
    base *= x  # multiply in each turn
    if not (a == power):  # if the range is not the end, print X base
        print("X", x, end=" ")

print("=", base)  # print the final answer

quit()
