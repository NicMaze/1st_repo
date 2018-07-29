def camel_case(string):
    return "".join([x.capitalize() for x in string.split()])

print(camel_case(" camel case word"))