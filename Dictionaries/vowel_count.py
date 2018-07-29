from collections import Counter

'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(values):
    start = []
    vowels = ['a','e','i','o','u']
    for x in values.lower():
        for y in vowels:
            if x == y:
                start.append(x)
    return Counter(start)

print(vowel_count('ColraACa'))