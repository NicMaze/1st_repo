#======= ZIP =========
nums1 = [1,2, 3,4,5]
num2={3,4,5}
print(dict(zip(nums1,num2))) # Numbers that can not zip are not returned (nums1[4,5])
#=====================
num3 = [(1, 4), (2, 5), (3, 3), (4, 2), (5, 1)]
unzip = list(zip(*num3))
print(unzip)
#======================
def interleave(str1, str2):
    new = list(zip(str1, str2))
    final = []
    for x in new:
        final += x
    return ''.join(final)

print(interleave("HI","Lo"))
#=======================
def triple_and_filter(nums):
    div_4 = [x for x in nums if x % 4 == 0]
    return [x*3 for x in div_4]

print(triple_and_filter([6,8,10,12])) # [24,36]