person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {k:v for k,v in person}
print(answer)

# OR using dict
answer2 = dict(person)
print(answer2)


# Create dictionary of vowels
answer3 = {i:0 for i in "aeiou"}
print(answer3)

answer4 = dict.fromkeys("aeiou", 0)
print(answer4)

# Create dictionary of range:chr(range)
answer5 = {i:chr(i) for i in range(65,91)}
print(answer5)