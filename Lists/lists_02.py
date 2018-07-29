sample_list = [1, 2, 3, 4]
# ADD TO LISTS
# append adds a single value
sample_list.append("Append/Pop")
# extend can add a list to a list
sample_list.extend([3, 2, 1])
# insert will add a value to a specific position. Example below would add to the end of a list;
# .insert(-1, "End") would result in [1, 2, 3, 4, 'Append value', 3, 2, 'End', 1]
sample_list.insert(len(sample_list), "End")
sample_list.insert(0, "Beginning")

# REMOVE FROM LISTS
# Clear will empty list
# sample_list.clear()
print(sample_list)
# pop will remove a value, with no index specified it will remove the last value
# You can create a new variable that returns what was removed using pop
removed_value = sample_list.pop(5) #removes position 4
print(f"This is what was removed using .pop --> '{removed_value}' <--")
print(sample_list)
# .remove() - looks for a value to remove, if multiple removes first position found.
# second_remove = sample_list.remove(3) this will return 'None' does not work like .pop()

# Index will give index position of value searched
first_one = sample_list.index(1)
print(f"Index of 1st #1 is {first_one}")
second_one = sample_list.index(1, (first_one + 1)) # finds index starting at position 3 to the end
print(f"Index of 2nd #1 is {second_one}, using starting index of (first + 1)")

remove_ends = sample_list[1:-1]
print(remove_ends)