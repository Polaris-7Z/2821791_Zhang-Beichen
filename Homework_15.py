# Asks for integers and calculates the median

numbers = []  # Create a list

while True:  # Asks for integers
    x = input("Number: ")
    if x == "done":
        break
    else:
        numbers.append(int(x))  # Add the number(integer) into the list

HL = int(len(numbers) / 2)  # Calculate half the length of the list

if len(numbers) % 2 == 0:  # The even list
    print("Median: ",  (numbers[HL-1] + numbers[HL]) / 2)
else:  # The odd list
    print("Median: ", numbers[HL])

quit()
