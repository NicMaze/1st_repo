def intersection(list1, list2):
    """Returned in list format and '&' will do intersection of sets"""
    return list(set(list1) & set(list2))

"""Alternate Solution"""
"""
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]
"""
print(intersection([123, 145, 555], [123, 133, 190, 555]))
# ===========================================================

'''
partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(num):
    return num % 2 == 0

def partition(lst, fn=isEven):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

print(partition([1,2,3,4]))

