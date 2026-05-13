from math import sqrt

myList = []
tot = 0

n = int(input("Enter the Number of items: "))

print("Enter", n, "Items:")

for i in range(n):
    item = int(input())
    myList += [item]   # Append item to list
    tot += item        # Add item to total

# Mean
mean = tot / n

# Variance
tot = 0

for item in myList:
    tot += (item - mean) * (item - mean)

var = tot / n

# Standard Deviation
std = sqrt(var)

# Output
print("Mean =", mean)
print("Variance =", var)
print("Standard Deviation =", std)