# Set Comprehension
# range of 0-9 x itself, sets not in order
range_set = {x*x for x in range(10)}
print(range_set)
# Upper case each unique value
upper_set = {char.upper() for char in "bIg booty JUDY"}
print(upper_set)

def all_vowels_in_string(string):
    len({char for char in string if char in 'aeiou'})==5

tree = "aeiou"

if all_vowels_in_string(tree) == True:
    print("You did it")
else:
    print("i'm lost")
