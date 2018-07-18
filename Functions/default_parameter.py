# Variables in function are Parameters
# When calling the function the variables are Arguments
# Why use Default Params:
#   Allows you to be more defensive
#   Avoids errors with incorrect paramaters
#   More readable examples!
#   Default paramaters need to be declared at the end if all are not defined
def exponent(num, power=2):
    """Exponent Function returns num ** power; default param is 2"""
    return num ** power

print(f"With Arguments {exponent(3, 3)}")
print(f"With Default Parameters {exponent(3)}")

def add(a=5, b=5):
    return (a + b)

print(f"With Arguments {add(3,3)}")
print(f"With Default Parameters {add()}")
print(f"With Keyword Arguments {add(b=99, a=22)}")

# Return doc string of function """ """
print(exponent.__doc__)