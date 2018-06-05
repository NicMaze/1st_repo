# for x in range(1, 21):
#     if (x == 4) or (x == 13):
#         state = "unlucky"
#     elif x % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{x} is {state}")
#=================================================
# nickname = ""
# while nickname != "bubba":
#     nickname = input("What is your nickname: ").lower()
# print("Loop breaks with correct nickname and it moves to this print statement")
#=================================================
# num = 10
# while num > 0:
#     print(f"{num} greater than 0")
#     num -= 1
# print(f"{num} now = 0")
#=================================================
# happyface = "\U0001f600"
# for x in range(10):
#     print(happyface * x)
#=================================================
copy_cat = input("Hey how's it going? ")

while copy_cat != "stop copying me":
    print(copy_cat)
    copy_cat = input()
print("you win :(")