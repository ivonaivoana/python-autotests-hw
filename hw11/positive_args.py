"""
Simple decorator to validate positive arguments.
"""


def validate_arguments(func):
    """Raise error if any argument is non-positive."""

    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Arguments must be positive")
        return func(*args)
    return wrapper


@validate_arguments
def sum_args(*args):
    """Return sum of all arguments."""

    return sum(args)


print(sum_args(1, 2, 3))
print(sum_args(1, -2, 3))
