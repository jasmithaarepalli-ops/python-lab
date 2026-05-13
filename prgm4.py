# Program to sort tuples based on second element

data = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_data = sorted(data, key=lambda x: x[1])

print("Sorted Data:", sorted_data)