'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(lst):
    for x in lst:
        if type(x) != list:
            return False
    return True

print(list_check([[],[1],[2,3], (1,2)]))