# Create nested list
one_two_three = [[num for num in range(1,4)] for val in range(1,4)]
print(one_two_three)
print("=====")
# Loop through nested loop. [[Loop through each value] Loop for each nested list]
evens = [[num for num in val if num % 2 == 0] for val in one_two_three]
print(evens)