#!/usr/bin/python
# Using decorators

# It is entirely optional for decorators to return the same function passed to
# them or not return anything.

###############################################################################
# Basic function decorator
# Here mydeco() is a function that can be used as a decorator for another
# function.
###############################################################################
print("*** Using basic function decorator")
def mydeco(fn):
    print("Hello, I am decorator for %s" % fn)
    return fn

@mydeco
def funcall():
    print("Hello, I am function itself")

# Call funcall() translates in to mydeco(funcall)
# mydeco() again returns the passed function which is funcall so it gets
# executed too.

funcall()


###############################################################################
# Decorator for a function with args
# deco_with_args() is a function that can be used as decorator for another
# function that accepts args
###############################################################################
print("*** Using decorator for a function with args")
def deco_with_args(fn):
    def wrapper(*args):
        print("Calling %s with %s" % (fn, args))
        return fn(*args)
    return wrapper

@deco_with_args
def func_with_args(x, y):
    print("Got the args: %s, %s" % (x, y))

# Call func_with_args(10, 20) translates in to deco_with_args(func_with_args)(10, 20)
# deco_with_args(func_with_args) returns wrapper so it will become wrapper(10, 20)
# wrapper(10, 20) again returns func_with_args(10, 20)

func_with_args(10, 20)


###############################################################################
# Decorator with args
# Decorator that accepts args for itself
###############################################################################
print("*** Using decorator with args on a function")
def deco_args(a, b):
    def wrapper(fn):
        print("Decorator args: %d, %d" % (a, b))
        return fn
    return wrapper

@deco_args(10, 20)
def test_fun():
    print("Inside test_fun()")

test_fun()

###############################################################################
# Class decorator
###############################################################################
print("*** Using class decorators")
class Decorator:
    def __init__(self, fn):
        self._fn = fn

    def __call__(self, *args):
        print("Hello, you are asking for sum of %d, %d, right ?" % args)
        print(self._fn(*args))

@Decorator
def sum(a, b):
    """Returns the sum of a, b"""
    print("Calculating the sum of %d, %d" % (a, b))
    return a + b

# Here, the function 'sum' will be assigned to self._fn on Decorator instance.
# And since it has __call__(), instance of Decorator can be called.
# Decorator instance call returns self._fn with args passed so it then executes
# body of sum()
sum(24, 36)
