"""
A decorator that checks the function's return value
and prints out a message if the return value is not an integer
"""


def check_isint(func):
    """Print message if result is not int"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, int):
            print("The result is not int")
        return result

    return wrapper


@check_isint
def add(a, b):
    """Returns sum of two numbers"""
    return a + b


@check_isint
def greet(name):
    """Returns a greeting string"""
    return f"Hello {name}"


print(add(2, 3))
print(greet("Anna"))
