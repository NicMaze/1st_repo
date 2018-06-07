# List comprehension (multiply number)
start_list = [1, 2, 3]
multiply_ten = [x * 10 for x in start_list]
print(f"{start_list} is now {multiply_ten}")

# List comprehension (number to string)
num_list = range(1, 6)
# print num list in order as numbers
# create string_list variable of num_list using comprehension
string_list = [str(x) for x in num_list]
print(string_list)

# List comprehension for even, odd
evens = [num for num in num_list if num % 2 == 0]
odd = [num for num in num_list if num % 2 != 0]
print(f"Even: {evens} Odd: {odd}")


answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
print(answer)
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
print(answer2)
answer3 = [person[::-1].lower() for person in ["Elie", "Tim", "Matt"]]
print(answer3)
answer4 = [intersection for intersection in [1,2,3,4] if intersection in [3,4,5,6]]
print(answer4)
answer5 = [char for char in "amazing" if char not in "aeiou"]
print(answer5)