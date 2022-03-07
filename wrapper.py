
    # Assume we have this: Simple Decorator which takes a function’s output and puts it into a string, followed by three !!!!.

def mydeco(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!'
    return wrapper

    # Let’s now decorate two different functions with “mydeco”:

@mydeco
def add(a, b):
    '''Add two objects together, the long way'''
    return a + b

@mydeco
def mysum(*args):
    '''Sum any numbers together, the long way'''
    total = 0
    for one_item in args:
        total += one_item
    return total

    # when run add(10,20), mysum(1,2,3,4), it worked!

# >>> add(10,20)
# '30!!!'

# >>> mysum(1,2,3,4)
# '10!!!!'

    # However, the name attribute, which gives us the name of a function when we define it,

# >>>add.__name__
# 'wrapper`

# >>>mysum.__name__
# 'wrapper'

#     Worse

# >>> help(add)
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)

# >>> help(mysum)
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)

#     we can fix partially by:

def mydeco(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!'
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

    now we run step 5 (2nd time) again:

# >>> help(add)
# Help on function add in module __main__:

# add(*args, **kwargs)
#      Add two objects together, the long way

# >>> help(mysum)
# Help on function mysum in module __main__:

# mysum(*args, **kwargs)
#     Sum any numbers together, the long way

#     but we can use functools.wraps (decotator tool)

from functools import wraps

def mydeco(func):
    @wraps(func)
    def wrapper(*args, *kwargs):
        return f'{func(*args, **kwargs)}!!!'
    return wrapper

    now run step 5 (3rd time) again

# >>> help(add)
# Help on function add in module main:
# add(a, b)
#      Add two objects together, the long way

# >>> help(mysum)
# Help on function mysum in module main:
# mysum(*args)
#      Sum any numbers together, the long way

