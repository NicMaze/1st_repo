def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

def move_zeros(array):
    #return [x if x ==0 array.pop(x) else None for x in array]
    return [nonZero for nonZero in array if nonZero != 0] + \
           [Zero for Zero in array if Zero == 0]

print(move_zeros([1,2,0,3,'a',4]))

'''
results = map(lambda x: x*2, A)
array.append(array.pop(x)) if x == 0 else None)
myList = [ x if x%2 else x*100 for x in range(1, 10) ]
'''