"""
Decorator for typing arguments.
"""


def typed(type_):
    """Convert all function arguments to the specified type."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = tuple(type_(x) for x in args)
            new_kwargs = {k: type_(v) for k, v in kwargs.items()}
            return func(*new_args, **new_kwargs)
        return wrapper
    return decorator


@typed(type_=str)
def add_str(a, b):
    return a + b


@typed(type_=int)
def add_int(a, b, c):
    return a + b + c


@typed(type_=float)
def add_float(a, b, c):
    return a + b + c


print(add_str("3", 5))
print(add_str(5, 5))
print(add_str("a", "b"))
print(add_int(5, 6, 7))
print(add_float(0.1, 0.2, 0.4))
