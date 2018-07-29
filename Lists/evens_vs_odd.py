def even_vs_odd(numbers):
    # x loops over numbers list created by the split.
    # convert to int mod 2
    # e returns True for Even, False for Odd
    e = [int(x) % 2 == 0 for x in numbers.split(' ')]
    # Checks for a single value of True, if not returns index of False in e plus 1
    # +1 to start iteration at 1 instead of 0
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

print(even_vs_odd("2 4 7 8 10"))