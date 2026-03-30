"""
A caching decorator to store function results.
"""


def cache(func):
    """Cache function results based on arguments."""
    cached_results = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_results:
            return cached_results[key]
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
