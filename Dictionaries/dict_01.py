cat = {"first": "Ari", "last": "Maize", "type": "cat", "age": 12, "color": "white"}
all_values = ""
all_items = ""

for values in cat.values():
    all_values += f"{values}, "
print(all_values)
print("*" * 8)

fullname = f"{cat['first']} {cat['last']}"
print(fullname)
print("*" * 8)

for key, value in cat.items():
    all_items += (f"Key {key} : Value {value}. ")
print(all_items)

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = sum(donations.values())
print(total_donations)
