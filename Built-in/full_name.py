from collections import Counter
'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

print(extract_full_name(names))


def duplicate_count(text):
    count = 0
    list = {x:v for x,v in Counter(text.lower()).items() if v >= 2}
    for x in list.keys():
        count += 1
    return count

print(duplicate_count("Aaaa22222222222aa11"))