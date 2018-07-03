from random import randint


# function structure
def sing_happy_birthday(name):
    h1 = "Happy Birthday to you"
    h2 = (f"Happy Birthday dear {name}")
    return (h1 + "\n" + h1 + "\n" + h2 + "\n" + h1)


def sq_rt(num):
    return (num ** 2)


def coin_toss(num):
    outcome = ""
    while num > 0:
        value = randint(0, 1)
        num -= 1
        if value == 0:
            outcome += ("heads ")
        else:
            outcome += ("tails ")
    print(outcome)


print(sing_happy_birthday("Nick"))
print(sq_rt(9))
coin_toss(4)
