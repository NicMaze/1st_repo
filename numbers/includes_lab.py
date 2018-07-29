'''
includes([1, 2, 3], 1) # True
includes([1, 2, 3], 1, 2) # False
includes({ 'a': 1, 'b': 2 }, 1) # True
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(collection, value, index=0):
    if type(collection) == dict:
        find_value = [v for v in collection.values()]
        return bool([x for x in find_value[index::] if x == value])
    else:
        return bool([x for x in collection[index::] if x == value])

print(includes({ 'a': 1, 'b': 2 }, 1))