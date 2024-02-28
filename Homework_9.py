# a 4-digit number that is even and does not end with a 0
n = int(input("Give me a 4-digit number that is even and does not end with a 0: "))

# Nesting
if 1000 <= n <= 9999:
    if n % 2 == 0:
        if not (n % 10 == 0):
            print("GOOD!")
        else:
            print("BAD! BECAUSE IT ENDS WITH 0")
    else:
        print("BAD! BECAUSE IT IS NOT EVEN")
else:
    print("BAD! BECAUSE IT IS NOT 4 DIGITS")

# Boolean
if 1000 <= n <= 9999 and n % 2 == 0 and not (n % 10 == 0):
    print("GOOD!")
else:
    print("BAD!")


quit()