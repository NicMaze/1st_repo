
def multiply_even_numbers(list):
    """Multiply even numbers from a string input"""
    total = 1
    for x in list:
        if x % 2 == 0:
            total *= x
    return total

print(multiply_even_numbers([2, 3, 4, 5, 6]))
# ==================================================
def capitalize(w):
    """Capitalize first letter of string input"""
    return w.capitalize()

print(capitalize("westworld"))
# ==================================================
def compact(list):
    return [x for x in list if x]
    # if x ==> This is because some values, such as empty lists, are considered False when evaluated for a
    # boolean value. Non-empty lists are True.
print(compact([0,1,2,"",[], False, {}, None, "All done"]))