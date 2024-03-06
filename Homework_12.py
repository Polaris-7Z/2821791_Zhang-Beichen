# Calculate the sum of 1/n^2 from 1 until it each extra term is not too large

#  give the initial values
n = 1
sum = 0
term = 1

# calculate 1/n^2 from 1 until term > 0.0000000000001
while term > 0.0000000000001:
    term = 1 / n**2
    sum += term
    n += 1

print("Sum=", sum)  # print the final answer

quit()