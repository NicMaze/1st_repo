def contains_purple(*args):
    if "purple" in args:
        return True
    return False

print(contains_purple("123", "eee", True, False, 123))
# ================================================================
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

print(combine_words("nick", suffix="strong" ))

