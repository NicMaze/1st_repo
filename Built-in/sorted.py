numbers = [2, 5, 3, 5, 7, 6, 4]
# Returns iterable item in a sorted list
print(sorted(numbers))
# Works on Tuples
tuple01 = (1, 3, 5, 4, 2)
print(tuple01)
# You can also sort in reverse order
print(f" Sorted Tuple {sorted(tuple01, reverse=True)}")

# Dictionary Sorted
chicago_bears = {"QB": "Mitch Trubisky", "RB": "Jordan Howard",
                 "Wide Receiver": "Allen Robinson", "Tight End": "Trey Burton"}

print(sorted(chicago_bears))
