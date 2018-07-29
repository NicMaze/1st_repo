'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(lst, num):
    list1 = lst
    list2 = lst
    for x in list1:
        for y in list2:
            if x == y:
                None
            elif x + y == num:
                return [x, y]
    return []

print(sum_pairs([4, 2, 1], 4))