from keyword import iskeyword

def contains_keyword(*args):
    for x in args:
        if iskeyword(x) == True:
            return True
    return False
#    return [iskeyword(x) for x in args]

