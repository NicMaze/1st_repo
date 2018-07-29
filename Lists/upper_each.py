def titleize(value):
    return " ".join([x[0].upper()+x[1:] for x in value.split(' ')])

print(titleize('this is awesome'))