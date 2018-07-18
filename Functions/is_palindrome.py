def is_palindrome(string):
    if string.lower().strip(" ") == string[::-1].lower().strip(" "):
        return True
    else:
        return False

print(is_palindrome("s Po  Op s"))
print(is_palindrome("RacecaR"))
print(is_palindrome("ChicaG0Be@r$"))
# ==================================================
'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list, st):
    total = [x for x in list if x == st]
    return len(total)

print(frequency([1,2,3,4,4,4], 4))

"""
^^^ My solution above ^^^
vvv Better way vvv
Using the built-in count() method, this is really nice and easy:

def frequency(collection, searchTerm):
    return collection.count(searchTerm)
"""