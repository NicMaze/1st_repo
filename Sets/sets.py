list_with_duplicates = [False, "Audi", "Scion", "Scion", "Chevy", False, 3.333]
print(f"Normal list {list_with_duplicates}")

# sets are not in order and it does not maintain duplicate entries
no_dups_set = set(list_with_duplicates)
print(f"Converted to 'set' {no_dups_set}")

# To maintain list format and remove dups
no_dups_list = list(set(list_with_duplicates))
print(f"Use set to remove dups and keep list format {no_dups_list}")

# Set methods
no_dups_set.add("Scion")        # Will not add duplicate
no_dups_set.add(10)             # .add will add value
print(f"Using .add method {no_dups_set}")
no_dups_set.remove("Chevy")     # .remove will remove item (If item does not exist this will generate an error
no_dups_set.discard(True)       # .discard will not generate an error if value doesn't exist
print(f"Using .remove/.discard method {no_dups_set}")
copy_set = no_dups_set.copy()   # Copy method to new value... copy_set is not the same as no_dups_set
print(copy_set)
copy_set.clear()                # Clear set
print(copy_set)                 # Validation - Copy is new set, changes do not impact original copy
print(no_dups_set)

# Math for sets
list1 = {"Nick", "Sophia", "Frank", "Ari", True, 33}
list2 = {"Nick", "Sophia", True, True, 33, 33, 40}
master_list = list1.union(list2)    # Union will combine each set
master_list1 = list1 | list2        # Pipe does returns the same value as union
master_list2 = list1 & list2        # & will do intersection
print(master_list)
print(master_list1)
print(master_list2)
