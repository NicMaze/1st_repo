range_list = list(range(1, 10))

# For loop over list
for evens in range_list:
    if evens % 2 == 0:
        print(evens)
print("end of 'FOR' loop example \n")
# While loop iterating over list (Using Index)
index = 0   # Need index point for while loop so it has an end; < length is important as well
            # <= results in error since index is now out of range...

while index <= len(range_list):
    print(range_list[index])
    index += 1



