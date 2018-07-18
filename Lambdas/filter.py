names = ["Mary", " Sean", "Jim", "Mike", "Molly", "Randy"]

def m_names(list01):
    return list(filter(lambda x: x[0]=="M", list01))

print(m_names(names))


# Remove negative numbers using lamda/filter
def remove_negatives(list1):
    return list(filter(lambda num: num >= 0, list1))

print(remove_negatives([1, 4, -11, 22, -1]))