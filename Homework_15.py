# Asks for integers and calculates the median

numbers = []  # Create a list

while True:  # Asks for integers
    x = input("Number: ")
    if x == "done":
        break
    else:
        numbers.append(int(x))  # Add the number(integer) into the list

length = int(len(numbers) / 2)  # Calculate the length of the list

if length % 2 == 0:  # The even list
    print("Median: ",  (numbers[length-1] + numbers[length]) / 2)
else:  # The odd list
    print("Median: ", numbers[length])

quit()
