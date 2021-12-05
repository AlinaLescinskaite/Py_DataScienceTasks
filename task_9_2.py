"""
Create a decorator called debug that will display information about the
function name, the parameters passed, and the result returned when
calling the function.
"""

import inspect


def debug(function):
    def wrapper(*args, **kwargs):
        func_args = inspect.signature(function).bind(*args, **kwargs).arguments
        func_args_str = ", ".join(map("{0[0]}={0[1]!r}".format, func_args.items()))
        print(f"Function {function.__name__} ({func_args_str}) returned {function(*args, **kwargs)}")
        return function(*args, **kwargs)
    return wrapper


@debug
def func(a, b, c):
    return a + b * c


if __name__ == '__main__':

    print(func(3, b=2, c=4))

