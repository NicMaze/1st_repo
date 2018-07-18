# abs = Absolute value of itself
print(abs(-33))
print(abs(33))

# Sum = Sum of number starting point is 0 but you can configure start point
# Can't sum string
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 10)) #Starting at 10 + list

# Round = Returns rounded number
print(round(3.33333))
print(round(3.33333, 2)) # Round number to 2nd position


def max_magnitude(nums):
    absolute = [abs(x) for x in nums]
    return max(absolute)
'''
def max_magnitude(nums):
return max(abs(num) for num in nums) #Slightly better code
'''
print(max_magnitude([1,2,3,4,-55, 3]))