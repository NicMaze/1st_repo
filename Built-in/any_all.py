# All will return true IF all items are True, otherwise False
def is_all_strings(lst):
    return all(type(str01) == str for str01 in lst)

# Any will return True IF any items are True