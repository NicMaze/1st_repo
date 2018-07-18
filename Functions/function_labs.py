days_of_the_week = {1:"Sunday", 2:"Monday"}
print(days_of_the_week[1])
# ============================================================
list = False
def last_element(a):
    if a:
        return a[-1]
    else:
        return None

print(last_element(list))
# ============================================================
def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Numbers are equal"


# ============================================================
def single_letter_count(word, position):
    value = word.lower().count(position.lower())
    return value

print(single_letter_count("HelLo World", "o"))
# ============================================================
'''
I used a dictionary comprehension. For each letter in the input string, I make the key the letter itself 
("a" for example), and the corresponding value is the result of running count() of that letter in the string.
'''
def multiple_letter_count(string):
    return {x:string.count(x) for x in string}

print(multiple_letter_count("awesome"))